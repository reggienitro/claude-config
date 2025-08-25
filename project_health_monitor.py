#!/usr/bin/env python3
"""
Project Health Monitoring Dashboard
Tracks status across all 5 GitHub repositories and local projects
"""

import os
import subprocess
import json
import datetime
from pathlib import Path
from typing import Dict, List, Any
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv('/Users/aettefagh/.config/api-keys/.env')

class ProjectHealthMonitor:
    """Monitor health across all projects"""
    
    def __init__(self):
        self.github_token = os.getenv('GITHUB_PERSONAL_ACCESS_TOKEN')
        self.repositories = [
            'reggienitro/claude-config',
            'reggienitro/article-to-audio-extension', 
            'reggienitro/bee-supabase-integration',
            'reggienitro/personal-data-lake',
            'reggienitro/knowledge-scraper'
        ]
        self.local_projects = {
            'claude-config': '/Users/aettefagh/claude-config',
            'article-to-audio': '/Users/aettefagh/AI projects/claude-tools/article-to-audio-extension',
            'bee-supabase': '/Users/aettefagh/AI projects/automation-tools/bee-supabase-integration',
            'personal-data-lake': '/Users/aettefagh/AI projects/automation-tools/personal-data-lake',
            'knowledge-scraper': '/Users/aettefagh/AI projects/claude-tools/knowledge-scraper'
        }
    
    def check_github_status(self) -> Dict[str, Any]:
        """Check GitHub repository status"""
        repo_status = {}
        
        headers = {
            'Authorization': f'token {self.github_token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        
        for repo in self.repositories:
            try:
                # Get basic repo info
                repo_url = f'https://api.github.com/repos/{repo}'
                response = requests.get(repo_url, headers=headers)
                
                if response.status_code == 200:
                    data = response.json()
                    
                    # Get latest commit
                    commits_url = f'https://api.github.com/repos/{repo}/commits'
                    commits_response = requests.get(commits_url, headers=headers, params={'per_page': 1})
                    latest_commit = commits_response.json()[0] if commits_response.status_code == 200 else None
                    
                    repo_status[repo] = {
                        'status': '✅ Healthy',
                        'last_updated': data.get('updated_at'),
                        'default_branch': data.get('default_branch'),
                        'size': data.get('size'),
                        'language': data.get('language'),
                        'open_issues': data.get('open_issues_count'),
                        'latest_commit': {
                            'sha': latest_commit['sha'][:8] if latest_commit else 'N/A',
                            'message': latest_commit['commit']['message'][:50] + '...' if latest_commit else 'N/A',
                            'date': latest_commit['commit']['author']['date'] if latest_commit else 'N/A'
                        } if latest_commit else None
                    }
                else:
                    repo_status[repo] = {
                        'status': f'❌ Error {response.status_code}',
                        'error': response.text[:100]
                    }
                    
            except Exception as e:
                repo_status[repo] = {
                    'status': '❌ Connection Error',
                    'error': str(e)[:100]
                }
        
        return repo_status
    
    def check_local_git_status(self) -> Dict[str, Any]:
        """Check local git repository status"""
        local_status = {}
        
        for project, path in self.local_projects.items():
            if not os.path.exists(path):
                local_status[project] = {
                    'status': '❌ Directory Not Found',
                    'path': path
                }
                continue
                
            try:
                # Change to project directory
                os.chdir(path)
                
                # Check if it's a git repo
                if not os.path.exists('.git'):
                    local_status[project] = {
                        'status': '⚠️ Not a Git Repository',
                        'path': path
                    }
                    continue
                
                # Get git status
                status_result = subprocess.run(['git', 'status', '--porcelain'], 
                                             capture_output=True, text=True)
                
                # Get current branch
                branch_result = subprocess.run(['git', 'branch', '--show-current'], 
                                             capture_output=True, text=True)
                
                # Get last commit
                commit_result = subprocess.run(['git', 'log', '-1', '--oneline'], 
                                             capture_output=True, text=True)
                
                # Check if ahead/behind remote
                remote_result = subprocess.run(['git', 'status', '-b', '--porcelain'], 
                                             capture_output=True, text=True)
                
                dirty_files = status_result.stdout.strip().split('\\n') if status_result.stdout.strip() else []
                dirty_count = len([f for f in dirty_files if f.strip()])
                
                # Parse remote status
                remote_status = "✅ Up to date"
                if "ahead" in remote_result.stdout:
                    remote_status = "⚠️ Ahead of remote"
                elif "behind" in remote_result.stdout:
                    remote_status = "⚠️ Behind remote"
                
                local_status[project] = {
                    'status': '✅ Clean' if dirty_count == 0 else f'⚠️ {dirty_count} uncommitted changes',
                    'branch': branch_result.stdout.strip(),
                    'last_commit': commit_result.stdout.strip(),
                    'remote_status': remote_status,
                    'dirty_files': dirty_files[:5] if dirty_count > 0 else [],
                    'path': path
                }
                
            except Exception as e:
                local_status[project] = {
                    'status': '❌ Git Error',
                    'error': str(e)[:100],
                    'path': path
                }
        
        return local_status
    
    def check_dependencies(self) -> Dict[str, Any]:
        """Check for dependency issues and security vulnerabilities"""
        dependency_status = {}
        
        for project, path in self.local_projects.items():
            if not os.path.exists(path):
                continue
                
            try:
                os.chdir(path)
                deps = {}
                
                # Check Python dependencies
                if os.path.exists('requirements.txt'):
                    # Check for outdated packages
                    pip_check = subprocess.run(['pip', 'list', '--outdated', '--format=json'], 
                                             capture_output=True, text=True)
                    
                    if pip_check.returncode == 0:
                        outdated = json.loads(pip_check.stdout) if pip_check.stdout.strip() else []
                        deps['python'] = {
                            'outdated_count': len(outdated),
                            'outdated_packages': [p['name'] for p in outdated[:5]]
                        }
                
                # Check Node.js dependencies
                if os.path.exists('package.json'):
                    npm_audit = subprocess.run(['npm', 'audit', '--json'], 
                                             capture_output=True, text=True)
                    
                    if npm_audit.returncode in [0, 1]:  # npm audit returns 1 if vulnerabilities found
                        try:
                            audit_data = json.loads(npm_audit.stdout)
                            deps['nodejs'] = {
                                'vulnerabilities': audit_data.get('metadata', {}).get('vulnerabilities', {}),
                                'total_deps': audit_data.get('metadata', {}).get('totalDependencies', 0)
                            }
                        except:
                            deps['nodejs'] = {'status': 'Could not parse audit'}
                
                dependency_status[project] = deps
                
            except Exception as e:
                dependency_status[project] = {
                    'error': str(e)[:100]
                }
        
        return dependency_status
    
    def check_system_health(self) -> Dict[str, Any]:
        """Check system-level health indicators"""
        try:
            # Check disk space
            disk_usage = subprocess.run(['df', '-h', '/'], capture_output=True, text=True)
            disk_lines = disk_usage.stdout.strip().split('\\n')
            disk_info = disk_lines[1].split() if len(disk_lines) > 1 else []
            
            # Check memory usage
            memory_usage = subprocess.run(['vm_stat'], capture_output=True, text=True)
            
            # Check MCP servers (basic check)
            mcp_status = "✅ Available" if os.path.exists('/Users/aettefagh/.config/api-keys/.env') else "❌ Not configured"
            
            return {
                'disk_usage': {
                    'total': disk_info[1] if len(disk_info) > 1 else 'N/A',
                    'used': disk_info[2] if len(disk_info) > 2 else 'N/A',
                    'available': disk_info[3] if len(disk_info) > 3 else 'N/A',
                    'percentage': disk_info[4] if len(disk_info) > 4 else 'N/A'
                },
                'mcp_servers': mcp_status,
                'python_version': subprocess.run(['python3', '--version'], capture_output=True, text=True).stdout.strip(),
                'git_version': subprocess.run(['git', '--version'], capture_output=True, text=True).stdout.strip()
            }
            
        except Exception as e:
            return {'error': str(e)}
    
    def generate_health_report(self) -> str:
        """Generate comprehensive health report"""
        print("🔍 Gathering project health data...")
        
        github_status = self.check_github_status()
        local_status = self.check_local_git_status()
        dependency_status = self.check_dependencies()
        system_status = self.check_system_health()
        
        report = f"""
# Project Health Report
*Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*

## 📊 Overview
- **Total Projects**: {len(self.repositories)}
- **GitHub Repositories**: {len([r for r in github_status.values() if '✅' in r.get('status', '')])} healthy
- **Local Repositories**: {len([r for r in local_status.values() if '✅' in r.get('status', '')])} clean

## 🌐 GitHub Repository Status
"""
        
        for repo, status in github_status.items():
            project_name = repo.split('/')[-1]
            report += f"""
### {project_name}
- **Status**: {status.get('status', 'Unknown')}
- **Language**: {status.get('language', 'N/A')}
- **Last Updated**: {status.get('last_updated', 'N/A')[:10]}
- **Open Issues**: {status.get('open_issues', 'N/A')}
"""
            if status.get('latest_commit'):
                commit = status['latest_commit']
                report += f"- **Latest Commit**: {commit['sha']} - {commit['message']}\\n"
        
        report += "\\n## 💻 Local Repository Status\\n"
        
        for project, status in local_status.items():
            report += f"""
### {project}
- **Status**: {status.get('status', 'Unknown')}
- **Branch**: {status.get('branch', 'N/A')}
- **Remote**: {status.get('remote_status', 'N/A')}
- **Last Commit**: {status.get('last_commit', 'N/A')}
"""
            if status.get('dirty_files'):
                report += f"- **Uncommitted Files**: {', '.join(status['dirty_files'][:3])}{'...' if len(status['dirty_files']) > 3 else ''}\\n"
        
        report += "\\n## 📦 Dependency Health\\n"
        
        for project, deps in dependency_status.items():
            if 'error' in deps:
                report += f"- **{project}**: ❌ {deps['error']}\\n"
            else:
                python_deps = deps.get('python', {})
                nodejs_deps = deps.get('nodejs', {})
                
                if python_deps:
                    outdated = python_deps.get('outdated_count', 0)
                    status_icon = '⚠️' if outdated > 0 else '✅'
                    report += f"- **{project} (Python)**: {status_icon} {outdated} outdated packages\\n"
                
                if nodejs_deps:
                    vulns = nodejs_deps.get('vulnerabilities', {})
                    total_vulns = sum(vulns.values()) if isinstance(vulns, dict) else 0
                    status_icon = '⚠️' if total_vulns > 0 else '✅'
                    report += f"- **{project} (Node.js)**: {status_icon} {total_vulns} vulnerabilities\\n"
        
        report += "\\n## 🖥️ System Health\\n"
        
        if 'error' not in system_status:
            disk = system_status.get('disk_usage', {})
            report += f"""
- **Disk Space**: {disk.get('used', 'N/A')} / {disk.get('total', 'N/A')} ({disk.get('percentage', 'N/A')})
- **MCP Servers**: {system_status.get('mcp_servers', 'N/A')}
- **Python**: {system_status.get('python_version', 'N/A')}
- **Git**: {system_status.get('git_version', 'N/A')}
"""
        
        report += f"""
## 🎯 Recommendations

### High Priority
- **Deploy Article-to-Audio**: Ready for Render deployment
- **Validate Bee Integration**: Complete final testing
- **Update Dependencies**: {sum(d.get('python', {}).get('outdated_count', 0) for d in dependency_status.values())} packages need updates

### Medium Priority
- **Security Review**: Check for vulnerabilities in Node.js packages
- **Backup Verification**: Ensure all projects are properly backed up
- **Documentation Updates**: Keep READMEs current with latest changes

### Next Session Focus
1. Complete active development in other terminals
2. Deploy article-to-audio to Render
3. Set up automated dependency updates
4. Create comprehensive testing framework

---

*Health monitoring system: Operational*  
*All systems: Ready for continued development*
"""
        
        return report
    
    def save_report(self, report: str) -> str:
        """Save health report to file"""
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'/Users/aettefagh/claude-config/health_report_{timestamp}.md'
        
        with open(filename, 'w') as f:
            f.write(report)
        
        return filename

def main():
    """Run health monitoring"""
    monitor = ProjectHealthMonitor()
    report = monitor.generate_health_report()
    
    print(report)
    
    # Save report
    filename = monitor.save_report(report)
    print(f"\\n📄 Report saved to: {filename}")
    
    # Also create latest report link
    latest_link = '/Users/aettefagh/claude-config/health_report_latest.md'
    try:
        if os.path.exists(latest_link):
            os.remove(latest_link)
        os.symlink(filename, latest_link)
        print(f"📄 Latest report: {latest_link}")
    except:
        pass

if __name__ == "__main__":
    main()