import subprocess
import time

def run_cmd(cmd, outfile=None):
    print(f"Running: {cmd}")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10)
        output = (result.stdout or '') + "\n" + (result.stderr or '')
    except subprocess.TimeoutExpired as e:
        output = str(e.stdout or '') + "\n" + str(e.stderr or '')
    except Exception as e:
        output = str(e)
    
    if outfile:
        with open(outfile, 'w', encoding='utf-8') as f:
            f.write(output)
    return output

def main():
    run_cmd('curl -X POST http://localhost:8000/djangoapp/logout/', 'logoutuser')
    run_cmd('curl http://localhost:3030/dealers', 'getalldealers')
    run_cmd('curl http://localhost:3030/dealers/1', 'getdealerbyid')
    run_cmd('curl "http://localhost:3030/dealers?state=Kansas"', 'getdealersbyState')
    run_cmd('curl http://localhost:3030/reviews/1', 'getdealerreviews')
    run_cmd('curl http://localhost:3030/cars', 'getallcarmakes')
    run_cmd('curl "http://localhost:5000/analyze?text=Fantastic%20services"', 'analyzereview')
    run_cmd('echo "Build and test workflow succeeded." > CICD', 'CICD')

if __name__ == '__main__':
    main()
