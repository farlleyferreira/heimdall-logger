# :satellite: Heimdall Logger :satellite:

### Resumo

> <p style="text-align: justify"> 
> Este projeto foi desenvolvido como resultado de um estudo sobre sistemas assíncronos e, da necessidade de prover um serviço flexível, que pudesse ser 
> estendido a diversos cenários e formas de aplicação, podendo ser utilizado tanto para a finalidade de log's síncronos quanto assíncronos. As funcionalidades 
> do heimdall-logger serão mais bem discutidas nas seções pertinentes. Este módulo tem como objetivo permitir:
> </p>
>
> <ul>
> <li> Realizar logs de forma síncrona e assíncrona </li>
> <li> Realizar logs nos formatos LOG, TXT e JSON (Outros formatos serão implementados posteriormente) </li>
> <li> Realizar callback do log para api's de acordo com o a necessidade do usuário</li>
> </ul>
>
> <p style="text-align: justify"> 
> Ao longo do desenvolvimento do projeto, outras integrações poderão ser adicionadas, desde que, sejam efetuadas respeitando as diretrizes
> e padrões adotados neste projeto, esta decisão foi tomada com a finalidade de manter a integridade conceitual do projeto.  Sinta-se à vontade para
> contribuir com o mesmo.
> </p>

### Roadmap

</br>

> <ol>
> <li> Melhorar a funcionalidade de escrita para arquivos JSON. </li>
> <li> Melhoria e aumento da profundidade dos testes da aplicação. </li>
> <li> Implantação outros formatos de saída para os arquivos de log (Ex: XML, CSV). </li>
> <li> Adicionar funcionalidades de stream e funcionalidades de escrita mais personalizáveis. </li>
> <li> Implantação de prova de conceito para providers em bancos de dados. (SQL, MongoDB, MySQL, PostgreSQl, entre outros) </li>
> </ol>

### Setup

> <i><b>Para rodar o projeto heimdall-logger localmente.</b></i>
>
> <p style="text-align: justify"> 
>   <ol>
>    <li> Realize o clone desta aplicação para seu diretório de projetos</li>
>    <li> Certifique-se de possuir o make instalado em seu OS</li>
>    <li> Crie um ambiente virtual utilizando gerenciador de sua preferência > (pyenv, virtualenv, anaconda...).</li>
>    <li> Dentro deste diretório será possível verificar a criação da pasta: <i><b>heimdall-logger</b></i></li>
>    <li> Execute o comando:</b></i></li>
>   </ol>
> </p>
>
> ```bash
> make install-requeriments
> ```
>
> <i> &nbsp;&nbsp;&nbsp; ou caso não possua o make, poderá rodar o comando:</i>
>
> ```bash
> pip install -r requirements.txt
> ```
>
> Seguido de:
>
> ```bash
> pip install -r requirements-dev.txt
> ```
>
> <p style="text-align: justify"> 
>   <ol start="7">
>    <li> Se todos os pacotes foram instalados corretamente você poderá executar:</li>
>   </ol>
> </p>
>
> ```bash
> make run-demo
> ```
>
> Será possível observar no seu console, o log de todos os oito níveis existentes nesta lib sendo exibidos
>
> <i><b>Para rodar a suite de testes execute:</b></i>
>
> ```bash
> make test-coverage
> ```
>
> <i> &nbsp;&nbsp;&nbsp; ou caso não possua o make, poderá rodar o comando:</i>
>
> ```bash
> pytest --cov-report term-missing --cov=project/
> ```
>
> Ou ainda, de acordo com a preferência do desenvolvedor, os testes poderão ser executados via plugin da sua IDE
> ou editor de códigos preferida, recomendo a [Python Test Explorer for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=LittleFoxTeam.vscode-python-test-adapter) ou ainda [Test Explorer UI](https://marketplace.visualstudio.com/items?itemName=hbenl.vscode-test-explorer).

### Utilização

#### Para realizar a instalação do heimdall-logger:

> ```bash
> pip install heimdall-logger
> ```
>
> <p style="text-align: justify"> 
> Após realizar a instalação, você poderá importar as funcionalidades que utilizará para criar a instância de log, de acordo com sua necessidade. Ao importar o heimdall-logger, serão expostos os seguintes módulos:
>
> ```python
> from heimdall_logger import (
>   Extension,
>   Level,
>   FileDataLog,
>   ApiSendLog,
>   SyncLogger,
>   AsyncLogger
> )
> ```
>
> Tendo importado os módulos necessários para implantar o log no contexto desejado vamos instânciar todas as dependências da seguinte forma:
>
> Para gerarmos nosso arquivo de log utilizaremos o modulo FileDataLog (vide a seção Overview):
>
> ```python
> _log_file_data = FileDataLog(
>     log_extension=Extension.LOG,
>     log_name="[NOME_DESEJADO_PARA_O_ARQUIVO_DE_LOG]",
>     log_path="[CAMINHO_DESEJADO_PARA_GRAVAÇÃO_DO_LOG]"
> )
> ```
>
> Caso seja necessário podemos também chamar uma API e enviar nossos dados de log para ela da seguinte forma:
>
> ```python
> _api_send_log = ApiSendLog(
>     api_route="[ROTA_DA_API_A_QUAL_DESEJA_ENVIAR_O_LOG]",
>     api_method="[METODO_HTTP]",
>     api_headers="[CASO_PRECISE_ENVIE_OS_CABEÇALHOS_COMO_DICT]"
> )
> ```
>
> E finalmente criamos nossa instância de log:
>
> ```python
> sync_logger = SyncLogger(
>     project_name="[NOME_DO_PROJETO_EM_CONTEXTO]",
>     file_data=_log_file_data,
>     api_callback=_api_send_log
> )
> ```
>
> Ou então:
>
> ```python
> async_logger = AsyncLogger(
>     project_name="",
>     file_data=object,
>     api_callback=object
> )
> ```
>
> Perceba que não enviamos o atributo pattern em nenhuma das duas formas, isso se deve ao fato de que o padrão pré-configurado nos atende em todos os cenário, não sendo seu caso, é possível configurar um novo padrão da seguinte forma:
>
> padrão pré-configurado:
>
> ```python
> _pattern = "[{level}][{datetime}] - {transaction} - {project_name}.{class_name}.{function_name} - {message}"
>
> ```
>
> padrão customizado:
>
> ```python
> _pattern = "[{level}][{datetime}] | {transaction} | {project_name}_{class_name}_{function_name}: {message}"
>
> ```
>
> Desde que seja respeitado o nome dos parâmetros (level, datetime, transaction, project_name, class_name, function_name e message) o log será gravado no padrão que for mais conveniente ao seu proposito. Dito isto, basta enviar na instancia do SyncLogger ou do AsyncLogger, atributo "pattern" ao novo padrão desejado.
>
> Muito bem, configuramos nossa instancia de log com todas as possibilidades, para realizar o log, basta então chamar a função de log:
>
> ```python
> sync_logger.log(level=Level.INFO,message="MongoDB connection",transaction="start db connection")
> ```
>
> Ou então:
>
> ```python
> async_logger.log(level=Level.INFO,message="MongoDB connection",transaction="end dbconnection")
> ```
>
> No metodo log podemos enviar como parâmetro:
>
> ```yaml
> class.log:
>   - message = "[MENSAGEM_QUE_DESEJA_GRAVAR]"
>   - transaction = "[TAG_QUE_IDENTIFICA_O_ESTADO_DA_TRANSACAO]"
>   - level = Level.INFO | .CRITICAL | .DEBUG | .ERROR | .FATAL | .NOTICE | .TRACE | WARNING | UNSET
>   - error = Exception("um tipo qualquer de exceção")
> ```

### Overview

#### Significado e casos de uso de cada modulo:

> </p>
> <i><b>Extension:</b></i>
>
> <p style="text-align: justify"> 
>   O modulo Extension, é um enumerator que possui todos os formatos de arquivos que a biblioteca consegue processar. À medida que mais formatos forem adicionados, serão incluidos nesse modulo.
>
> ```yaml
> Extension:
>   - LOG
>   - TXT
>   - JSON
> ```
>
> </p>
> <i><b>Level:</b></i>
>
> <p style="text-align: justify"> 
>   Já no modulo Level, que também é um enumerator, expomos os diversos níveis de log com que o heimdall-logger trabalha.
>
> ```yaml
> Level:
>   - CRITICAL
>   - DEBUG
>   - ERROR
>   - FATAL
>   - INFO
>   - NOTICE
>   - TRACE
>   - WARNING
>   - UNSET
> ```
>
> </p>
> <i><b>FileDataLog:</b></i>
>
> <p style="text-align: justify"> 
> O módulo FileDataLog, permite especificar qual extensão de arquivo de log, gostaríamos que nossos dados fossem gravados, permite ainda que especifiquemos qual o nome do arquivo de log e em qual diretório este arquivo será gravado. Este módulo poderá ou não ser passado de acordo com o contexto de utilização dos módulos SyncLogger e AsyncLogger.
>
> ```python
> log_file_data = FileDataLog(
>     log_extension=Extension.JSON,
>     log_name="logfile",
>     log_path=""
> )
> ```
>
> </p>
> <i><b>ApiSendLog:</b></i>
>
> <p style="text-align: justify"> 
> O módulo ApiSendLog, permite realizar o log das informações, realizando uma chamada via protocolo http, na qual enviará a um recurso qualquer, as informações de log, de forma síncrona ou assíncrona. Para que tal ação seja possível, você deverá informar ao modulo, qual verbo http sua api utiliza, qual a rota, e caso exista algum parâmetro de cabeçalho, tal como um token de autorização, poderá ser enviado em api_headers.
>
> ```python
> api_send_log = ApiSendLog(
>     api_route="",
>     api_method="",
>     api_headers={}
> )
> ```
>
> <i><b>SyncLogger e AsyncLogger:</b></i>
>
> <p style="text-align: justify"> 
> Com o heimdall-logger, é possível realizar logs de forma síncrona (SyncLogger) ou assíncrona (AsyncLogger), você tem liberdade para utilizar ambos os modelos de acordo com o contexto o qual seu sistema se encontra, para isso, na instância do método você deverá informar o nome do projeto (este é um parâmetro obrigatório), poderá informar um provedor de escrita de arquivos e, também de envio de dados para uma api a seu critério. Caso, nosso padrão de log não atenda sua necessidade, você poderá customizar este padrão e enviar um template-string com o padrão desejado.
>
> ```python
> sync_logger = SyncLogger(
>     project_name="",
>     file_data=object,
>     api_callback=object,
>     pattern=""
> )
>
> async_logger = AsyncLogger(
>     project_name="",
>     file_data=object,
>     api_callback=object,
>     pattern=""
> )
> ```
>
> </p>
