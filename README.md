# annotation interface py

## Setup

- Suba os containers `docker-compose up`

### Docker image
Para criar ou atualizar um imagem, utilize `docker-compose build`. Tal comando também pode ser utilizado para
 atualizar as dependencias (requirements.txt) dentro do container.


## Testing
- `docker-compose exec app ./bin/ci.sh`


## Arquitetura
```console
$ tree -d -L 4 -I __pycache__ annotation_interface_py/
annotation_api/ # Subdominio da empresa / Contexto limitado (BC): Recursos relacionados a uma das linhas de negocios ou produtos da empresa
├── application # Camada que recebe uma entrada do mundo externo, manipula o domain e retorna algo para o mundo externo
├── domain # logica de negocios pura e simples, isto é, apenas classes que lidam diretamente com a resolução do problema que este BC visa resolver 
│   ├── model # modelagem dos dados e açoes para cada modelo do dominio
│   │   └── job_opening # Um dos modelos de nível superior
│   │       └── description # Um dos modelos de nivel inferior (seu ciclo de vida é totalmente dependente do modelo superior)
│   └── service # acoes mais complexas; manipulam mais de um elemento do modelo
└── infra # infraestrutura do BC. Aqui fica o codigo que faz a ponte entre a regra de negocios e os elementos de infraestrutura (banco de dados, cache, framework web, etc)
    └── domain
        └── model
```