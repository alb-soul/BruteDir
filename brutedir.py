import subprocess

def read_wordlist(file_path):
    with open(file_path, 'r') as f:
        return f.read().splitlines()

def make_request(curl_command):
    try:
        response = subprocess.check_output(curl_command, shell=True, text=True)
        return response
    except subprocess.CalledProcessError as e:
        return str(e)

def main():
    target_url = input("Masukkan URL target (contoh: example.com): ")
    wordlist_path = input("Masukkan path ke file wordlist (contoh: wordlist.txt atau /path/file.txt): ")
    print("\n")
    wordlist = read_wordlist(wordlist_path)

    for word in wordlist:
        directory_url = "https://" + target_url + "/" + word + "/"
        curl_command = f"curl -s -o /dev/null -w '%{{http_code}}' {directory_url}"
        status_code = make_request(curl_command)

        print(f"{directory_url} - Status code: {status_code}")

if __name__ == "__main__":
    main()
