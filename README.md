# ts-spm-plugin
Swift package manager for TrustSource (ECS) (open source code compliance)

> [!WARNING]
> **PLEASE NOTE:** We stopped further development on this tool. You may still use it, but it will no longe receive support. Starting Q4/2024 we decided to focus all efforts on developing [ts-scan](https://github.com/trustsource/ts-scan), which will soon also cover all capabilities of this solution. 


## Installation

#### Requirements

- **pip** - is often already contained in the Python distribution but in some cases, please, follow the pip's [installation instruction](https://pip.pypa.io/en/stable/installing/) 

#### Installation from a local folder

```markdown
cd <path to the ecs-spm-plugin>
pip install ./ --process-dependency-links
```

## Usage

```markdown
ecs-spm-plugin <path to the project directory>
```

#### Requirements

- **ecs-plugin.json** - settings file in the project's directory

## Project settings (ecs-plugin.json)

- **project** : String - project name
- **credentials** : String [optional] - location of the file containing login information (userName and appKey) for the ECS service. Ignored: if a userName or appKey keys are present in the config file
- **userName** : String - ECS login name
- **appKey** : String - ECS key for apps
- **skipTransfer** : Bool - outputs the scan results into the stdout without submitting to the ECS service

## License

[MIT](https://github.com/eacg-gmbh/ecs-spm-plugin/blob/master/LICENSE)
