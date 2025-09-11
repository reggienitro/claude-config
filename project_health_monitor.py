#!/usr/bin/env python3
"""
Project Health Monitoring Dashboard with Enhanced Type Safety
Tracks status across all 5 GitHub repositories and local projects
"""

import os
import subprocess
import json
import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple, TypedDict
from dataclasses import dataclass, field
from enum import Enum
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv('/Users/aettefagh/.config/api-keys/.env')

class HealthStatus(Enum):
    """Health status levels"""
    HEALTHY = "healthy"
    WARNING = "warning"
    ERROR = "error"
    UNKNOWN = "unknown"

class TestStatus(TypedDict):
    """Type definition for test results"""
    passed: int
    failed: int
    skipped: int
    total: int

class RepoInfo(TypedDict):
    """Type definition for repository information"""
    name: str
    stars: int
    forks: int
    open_issues: int
    last_push: str
    status: HealthStatus

class LocalProjectInfo(TypedDict):
    """Type definition for local project information"""
    path: str
    has_git: bool
    uncommitted_changes: int
    last_modified: str
    size_mb: float
    status: HealthStatus

@dataclass
class HealthReport:
    """Complete health report for all projects"""
    timestamp: datetime.datetime
    github_repos: Dict[str, RepoInfo] = field(default_factory=dict)
    local_projects: Dict[str, LocalProjectInfo] = field(default_factory=dict)
    mcp_servers: Dict[str, bool] = field(default_factory=dict)
    api_keys: Dict[str, bool] = field(default_factory=dict)
    overall_health: HealthStatus = HealthStatus.UNKNOWN
    recommendations: List[str] = field(default_factory=list)

class ProjectHealthMonitor:
    """Monitor health across all projects with type safety"""
    
    def __init__(self) -> None:
        self.github_token: Optional[str] = os.getenv('GITHUB_PERSONAL_ACCESS_TOKEN')
        self.repositories: List[str] = [
            'reggienitro/claude-config',
            'reggienitro/article-to-audio-extension', 
            'reggienitro/bee-supabase-integration',
            'reggienitro/personal-data-lake',
            'reggienitro/knowledge-scraper'
        ]
        self.local_projects: Dict[str, str] = {
            'claude-config': '/Users/aettefagh/claude-config',
            'article-to-audio': '/Users/aettefagh/AI projects/claude-tools/article-to-audio-extension',
            'bee-supabase': '/Users/aettefagh/AI projects/automation-tools/bee-supabase-integration',
            'personal-data-lake': '/Users/aettefagh/AI projects/automation-tools/personal-data-lake',
            'knowledge-scraper': '/Users/aettefagh/AI projects/claude-tools/knowledge-scraper'
        }
        self.mcp_servers: List[str] = [
            'filesystem', 'github', 'supabase', 'beemcp', 
            'memory', 'web-search', 'exa-search'
        ]
        self.required_api_keys: List[str] = [
            'GITHUB_PERSONAL_ACCESS_TOKEN',
            'SUPABASE_URL',
            'SUPABASE_KEY',
            'BEE_API_TOKEN',
            'EXA_API_KEY'
        ]
    
    def check_github_status(self) -> Dict[str, RepoInfo]:
        """Check GitHub repository status with type safety"""
        repo_status: Dict[str, RepoInfo] = {}
        
        if not self.github_token:
            print("⚠️  GitHub token not found")
            return repo_status
        
        headers: Dict[str, str] = {
            'Authorization': f'token {self.github_token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        
        for repo in self.repositories:
            try:
                # Get basic repo info
                url: str = f'https://api.github.com/repos/{repo}'
                response = requests.get(url, headers=headers)
                
                if response.status_code == 200:
                    data = response.json()
                    repo_status[repo] = RepoInfo(
                        name=data['name'],
                        stars=data['stargazers_count'],
                        forks=data['forks_count'],
                        open_issues=data['open_issues_count'],
                        last_push=data['pushed_at'],
                        status=self._determine_repo_health(data)
                    )
                else:
                    repo_status[repo] = RepoInfo(
                        name=repo.split('/')[-1],
                        stars=0,
                        forks=0,
                        open_issues=0,
                        last_push='unknown',
                        status=HealthStatus.ERROR
                    )
                    
            except Exception as e:
                print(f"❌ Error checking {repo}: {e}")
                repo_status[repo] = RepoInfo(
                    name=repo.split('/')[-1],
                    stars=0,
                    forks=0,
                    open_issues=0,
                    last_push='unknown',
                    status=HealthStatus.ERROR
                )
        
        return repo_status
    
    def _determine_repo_health(self, repo_data: Dict[str, Any]) -> HealthStatus:
        """Determine repository health status"""
        issues: int = repo_data.get('open_issues_count', 0)
        
        # Check last push date
        last_push_str: str = repo_data.get('pushed_at', '')
        if last_push_str:
            last_push = datetime.datetime.fromisoformat(last_push_str.replace('Z', '+00:00'))
            days_since_push: int = (datetime.datetime.now(datetime.timezone.utc) - last_push).days
            
            if days_since_push > 30:
                return HealthStatus.WARNING
            if issues > 10:
                return HealthStatus.WARNING
            
        return HealthStatus.HEALTHY
    
    def check_local_projects(self) -> Dict[str, LocalProjectInfo]:
        """Check local project status with type safety"""
        project_status: Dict[str, LocalProjectInfo] = {}
        
        for name, path_str in self.local_projects.items():
            path = Path(path_str)
            
            if not path.exists():
                project_status[name] = LocalProjectInfo(
                    path=path_str,
                    has_git=False,
                    uncommitted_changes=0,
                    last_modified='not found',
                    size_mb=0.0,
                    status=HealthStatus.ERROR
                )
                continue
            
            # Check git status
            has_git: bool = (path / '.git').exists()
            uncommitted: int = 0
            
            if has_git:
                try:
                    result = subprocess.run(
                        ['git', 'status', '--porcelain'],
                        cwd=path,
                        capture_output=True,
                        text=True
                    )
                    uncommitted = len(result.stdout.strip().split('\n')) if result.stdout.strip() else 0
                except:
                    pass
            
            # Get project size
            size_mb: float = self._get_directory_size(path)
            
            # Get last modified time
            last_modified: str = datetime.datetime.fromtimestamp(
                path.stat().st_mtime
            ).strftime('%Y-%m-%d %H:%M')
            
            # Determine health
            if uncommitted > 10:
                status = HealthStatus.WARNING
            elif not has_git:
                status = HealthStatus.WARNING
            else:
                status = HealthStatus.HEALTHY
            
            project_status[name] = LocalProjectInfo(
                path=path_str,
                has_git=has_git,
                uncommitted_changes=uncommitted,
                last_modified=last_modified,
                size_mb=size_mb,
                status=status
            )
        
        return project_status
    
    def _get_directory_size(self, path: Path) -> float:
        """Calculate directory size in MB"""
        total_size: int = 0
        try:
            for item in path.rglob('*'):
                if item.is_file() and not item.is_symlink():
                    total_size += item.stat().st_size
        except:
            pass
        return round(total_size / (1024 * 1024), 2)
    
    def check_mcp_servers(self) -> Dict[str, bool]:
        """Check MCP server availability"""
        server_status: Dict[str, bool] = {}
        
        # Check Claude desktop config
        config_path = Path.home() / 'Library' / 'Application Support' / 'Claude' / 'claude_desktop_config.json'
        
        if config_path.exists():
            try:
                config = json.loads(config_path.read_text())
                configured_servers = config.get('mcpServers', {})
                
                for server in self.mcp_servers:
                    server_status[server] = server in configured_servers
            except:
                for server in self.mcp_servers:
                    server_status[server] = False
        else:
            for server in self.mcp_servers:
                server_status[server] = False
        
        return server_status
    
    def check_api_keys(self) -> Dict[str, bool]:
        """Check if required API keys are configured"""
        key_status: Dict[str, bool] = {}
        
        for key_name in self.required_api_keys:
            key_status[key_name] = bool(os.getenv(key_name))
        
        return key_status
    
    def run_project_tests(self, project_path: str) -> Optional[TestStatus]:
        """Run tests for a project and return results"""
        path = Path(project_path)
        
        # Check for test files
        test_files: List[Path] = list(path.glob('**/test_*.py')) + list(path.glob('**/*_test.py'))
        
        if not test_files:
            return None
        
        try:
            # Run pytest if available
            result = subprocess.run(
                ['python', '-m', 'pytest', '--json-report', '--json-report-file=/tmp/test-report.json'],
                cwd=path,
                capture_output=True,
                text=True
            )
            
            # Parse test results
            if Path('/tmp/test-report.json').exists():
                report = json.loads(Path('/tmp/test-report.json').read_text())
                return TestStatus(
                    passed=report['summary'].get('passed', 0),
                    failed=report['summary'].get('failed', 0),
                    skipped=report['summary'].get('skipped', 0),
                    total=report['summary'].get('total', 0)
                )
        except:
            pass
        
        return None
    
    def generate_health_report(self) -> HealthReport:
        """Generate comprehensive health report"""
        report = HealthReport(timestamp=datetime.datetime.now())
        
        # Check all components
        print("🔍 Checking GitHub repositories...")
        report.github_repos = self.check_github_status()
        
        print("🔍 Checking local projects...")
        report.local_projects = self.check_local_projects()
        
        print("🔍 Checking MCP servers...")
        report.mcp_servers = self.check_mcp_servers()
        
        print("🔍 Checking API keys...")
        report.api_keys = self.check_api_keys()
        
        # Determine overall health
        error_count: int = 0
        warning_count: int = 0
        
        for repo in report.github_repos.values():
            if repo['status'] == HealthStatus.ERROR:
                error_count += 1
            elif repo['status'] == HealthStatus.WARNING:
                warning_count += 1
        
        for project in report.local_projects.values():
            if project['status'] == HealthStatus.ERROR:
                error_count += 1
            elif project['status'] == HealthStatus.WARNING:
                warning_count += 1
        
        # Generate recommendations
        if not all(report.api_keys.values()):
            report.recommendations.append("Configure missing API keys")
        
        if not all(report.mcp_servers.values()):
            report.recommendations.append("Install missing MCP servers")
        
        for name, project in report.local_projects.items():
            if project['uncommitted_changes'] > 5:
                report.recommendations.append(f"Commit changes in {name}")
        
        # Set overall health
        if error_count > 0:
            report.overall_health = HealthStatus.ERROR
        elif warning_count > 2:
            report.overall_health = HealthStatus.WARNING
        else:
            report.overall_health = HealthStatus.HEALTHY
        
        return report
    
    def display_report(self, report: HealthReport) -> None:
        """Display health report in formatted output"""
        print("\n" + "="*60)
        print(f"📊 PROJECT HEALTH REPORT - {report.timestamp.strftime('%Y-%m-%d %H:%M')}")
        print("="*60)
        
        # Overall status
        status_emoji: Dict[HealthStatus, str] = {
            HealthStatus.HEALTHY: "✅",
            HealthStatus.WARNING: "⚠️",
            HealthStatus.ERROR: "❌",
            HealthStatus.UNKNOWN: "❓"
        }
        
        print(f"\n🎯 Overall Health: {status_emoji[report.overall_health]} {report.overall_health.value.upper()}")
        
        # GitHub repositories
        print(f"\n📦 GitHub Repositories:")
        for repo_name, info in report.github_repos.items():
            print(f"  {status_emoji[info['status']]} {repo_name}")
            print(f"     ⭐ {info['stars']} | 🍴 {info['forks']} | 🐛 {info['open_issues']} issues")
        
        # Local projects
        print(f"\n💻 Local Projects:")
        for name, project_info in report.local_projects.items():
            print(f"  {status_emoji[project_info['status']]} {name}")
            print(f"     📁 {project_info['size_mb']}MB | {'🔧 Git' if project_info['has_git'] else '⚠️  No Git'} | 📝 {project_info['uncommitted_changes']} uncommitted")
        
        # MCP Servers
        print(f"\n🔌 MCP Servers:")
        for server, configured in report.mcp_servers.items():
            print(f"  {'✅' if configured else '❌'} {server}")
        
        # API Keys
        print(f"\n🔑 API Keys:")
        for key, configured in report.api_keys.items():
            print(f"  {'✅' if configured else '❌'} {key}")
        
        # Recommendations
        if report.recommendations:
            print(f"\n💡 Recommendations:")
            for rec in report.recommendations:
                print(f"  • {rec}")
        
        print("\n" + "="*60)
    
    def save_report(self, report: HealthReport, filename: Optional[str] = None) -> Path:
        """Save report to JSON file"""
        if not filename:
            filename = f"health-report-{report.timestamp.strftime('%Y%m%d-%H%M%S')}.json"
        
        reports_dir = Path.home() / "AI projects" / "health-reports"
        reports_dir.mkdir(exist_ok=True)
        
        report_path = reports_dir / filename
        
        # Convert report to dict
        report_dict = {
            'timestamp': report.timestamp.isoformat(),
            'overall_health': report.overall_health.value,
            'github_repos': report.github_repos,
            'local_projects': report.local_projects,
            'mcp_servers': report.mcp_servers,
            'api_keys': report.api_keys,
            'recommendations': report.recommendations
        }
        
        report_path.write_text(json.dumps(report_dict, indent=2))
        return report_path

def main() -> None:
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Monitor project health')
    parser.add_argument('--save', action='store_true', help='Save report to file')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    parser.add_argument('--quiet', action='store_true', help='Minimal output')
    
    args = parser.parse_args()
    
    monitor = ProjectHealthMonitor()
    report = monitor.generate_health_report()
    
    if args.json:
        report_dict = {
            'timestamp': report.timestamp.isoformat(),
            'overall_health': report.overall_health.value,
            'github_repos': report.github_repos,
            'local_projects': report.local_projects,
            'mcp_servers': report.mcp_servers,
            'api_keys': report.api_keys,
            'recommendations': report.recommendations
        }
        print(json.dumps(report_dict, indent=2))
    elif not args.quiet:
        monitor.display_report(report)
    
    if args.save:
        saved_path = monitor.save_report(report)
        print(f"\n💾 Report saved to: {saved_path}")
    
    # Exit with appropriate code
    if report.overall_health == HealthStatus.ERROR:
        exit(2)
    elif report.overall_health == HealthStatus.WARNING:
        exit(1)
    else:
        exit(0)

if __name__ == '__main__':
    main()