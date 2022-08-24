# Navigate to project directory
cd ~/data-engineering-aws/

# Pull changes from Git
git fetch --all

# WARNING: This discards all local changes!
# (for production EC2 only, not for dev)
git reset --hard HEAD
git pull

# Navigate to server directory
cd ~/data-engineering-aws/python-flask-server/

# Make scripts executable
chmod u+x server-config.sh
chmod u+x server-run.sh

# Run server-config.sh in case there are new config dependencies
./server-config.sh

# Run Flask HTTP server
python3 -m swagger_server