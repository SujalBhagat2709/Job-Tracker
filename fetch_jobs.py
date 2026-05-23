import requests

def fetch_jobs(keyword):

    url = f"https://remotive.com/api/remote-jobs?search={keyword}"

    response = requests.get(url)

    return response.json()


if __name__ == "__main__":

    keyword = input("Enter skill: ")

    jobs = fetch_jobs(keyword)

    print(f"Found {len(jobs['jobs'])} jobs")