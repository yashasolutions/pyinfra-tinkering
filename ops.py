from pyinfra.operations import server, files

ergo_release = "https://github.com/ergochat/ergo/releases/download/v2.11.1/ergo-2.11.1-linux-arm64.tar.gz"

def create_user():
    # Create a user
    server.user(
        name="create ergo user",
        user="ergo",
        home="/home/ergo",
        shell="/bin/bash",
        ensure_home=True,
        _sudo=True,
        _use_sudo_password=False
        )

def install_ergo():
    # Download Ergo release
    files.download(
        name="Download Ergo release",
        src=ergo_release,
        dest="/tmp/ergo.tar.gz",
        )

    server.shell(
        name="Extract Ergo release",
        commands=["tar -xvf /tmp/ergo.tar.gz -C /home/ergo/"],
        _sudo=True,
        _sudo_user="ergo",
        )

create_user()
install_ergo()

# # start the Ergo server
# files.link(
#     name="Create a symlink to the config file",
#     path="/home/ergo/default.conf",
#     target="/home/ergo/ircd.conf",
#     _sudo=True,
#     _sudo_user="ergo",
# )

# server.shell(
#     name="Start Ergo server",
#     commands=["/home/ergo/ergo-2.11.1/ergo mkcerts",
#               "/home/ergo/ergo-2.11.1/ergo run"],
#     _sudo=True,
#     _sudo_user="ergo",
# )
