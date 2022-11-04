import os
import time
os.environ["CGO_ENABLED"] = "0"
os.environ["GOARCH"] = "amd64"

# darwin, windows, linux
os.environ["GOOS"] = "windows"
awsKey = ""
awsSecret = ""
keys = f"-X 'main.awsKey={awsKey}' -X 'main.awsSecret={awsSecret}'"

has = os.popen("git log -n1 --format=format:%H")

LDFLAGS = f"-X 'main.buildTime={time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))}' " \
          f"-X 'main.version=1.1.{time.strftime('%Y%m%d', time.localtime(time.time()))}'"

if awsKey != "" and awsSecret != "":
    LDFLAGS += " " + keys

os.system(f"go build -ldflags \"-w -s {LDFLAGS}\"")




