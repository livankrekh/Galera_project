#京セラ様向けの画像認識WEBアプリ
##Installation
1. Download and install Docker Desktop from https://docs.docker.com/docker-for-windows/install/
2. Make sure it's running, go to General Settings and `Use the WSL 2 based engine` option is checked

##Usage
1. Make sure you are in a root directory of the project and open a terminal
2. Initially or when you've made changes to the project, run `docker-compose build`
3. To launch the application run `docker-compose up` (execute `docker-compose up --build` to build and run)
4. To apply new changes or to shutdown the application execute `docker-compose down`

To access the application go to url `http://localhost`
