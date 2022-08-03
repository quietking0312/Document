import os
os.environ["CGO_ENABLED"] = "0"
os.environ["GOARCH"] = "amd64"

# darwin, windows, linux
os.environ["GOOS"] = "linux"


os.system("go build")
