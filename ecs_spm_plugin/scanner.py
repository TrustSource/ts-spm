import json, subprocess

class Scanner:
    def __init__(self, client):
        self._client = client

    def run(self):

        cmd = ['swift', 'package', 'show-dependencies', '--format', 'json']
        result = subprocess.Popen(cmd, cwd=self._client.scanPath, stdout=subprocess.PIPE).communicate()[0]

        pkgInfo = json.loads(result)

        mod = pkgInfo.get('name','')

        scanInfo = {
            'project': self._client.projectName,
            'module': mod,
            'moduleId': 'spm:' + mod,
            'dependencies': [self._process_dependency(dep) for dep in pkgInfo.get('dependencies', [])]
        }

        return scanInfo

    def _process_dependency(self, depInfo):
        name = depInfo.get('name', '')

        version = depInfo.get('version', None)
        if version is None:
            versions = []
        else:
            versions = [version]

        dep = {
            'name' : name,
            'key' : 'spm:' + name,
            'versions' : versions,
            'description': '',
            'private': False,
            'homepageUrl': '',
            'repoUrl': depInfo.get('url', ''),
            'checksum': '',
            'licenses': [],
            'dependencies': [self._process_dependency(dep) for dep in depInfo.get('dependencies', [])]
        }

        return dep

