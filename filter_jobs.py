from fetch_jobs import fetch_jobs

def filter_remote_jobs(keyword):

    data = fetch_jobs(keyword)

    jobs = data["jobs"]

    for job in jobs[:5]:

        print("\nTitle:", job["title"])
        print("Company:", job["company_name"])
        print("Location:", job["candidate_required_location"])


if __name__ == "__main__":

    skill = input("Enter skill: ")

    filter_remote_jobs(skill)