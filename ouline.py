#import beautifulsoup and request here
import requests

#function to get job list from url 'https://www.monster.com/jobs/search?q={role}&where={location}'
def getJobList(role,location):
    url = 'https://www.monster.com/jobs/search?q={role}&where={location}'
    # Complete the missing part of this function here

#save data in JSON file
def saveDataInJSON(jobDetails):
    #Complete the missing part of this function here
    print("Saving jobDetails data to JSON")

#main function
def main():
    # Write a code here to get job location and role from user e.g. role = input()
    print("Enter role you want to search")
    role = input()
    # Complete the missing part of this function here
    
if __name__ == '__main__':
    main()


url = "https://www.indeed.com/jobs?q=Software Developer&l=Charlotte"
payload={}
headers = {
  'Cookie': 'CSRF=ojIJVoKITjWihgD00Wsw8og5Hc1D9jjy; CTK=1g9ittdkais2a802; __cf_bm=3d_3hEaWqjebPYFH1ZB06COXFyW1h_t1qMxR6wPYVdg-1659566470-0-ATYe9fdCDReSZ5kyzgvbicC+JDlKwhgvFvGSbDDdko6JkHClfUeUHJ1EFMuOs16qJbo4Dv9qQTMbCUystHtrkYY=; _cfuvid=8bi6jLjOgpRdvOI8aEyezfmaUd9mO0LufOGoH05eHQU-1659566470830-0-604800000; CTK=1g9ittdkais2a802; INDEED_CSRF_TOKEN=V52DfhCraHkJ3bBxqz5X2GaEbJSI4o9L; JSESSIONID=5665C2F454B693F196A77CE7BAE6B2FE; LV="LA=1659566470:CV=1659566470:TS=1659566470"; PREF="TM=1659566529355:L=Charlotte"; RQ="q=Software+Developer&l=Charlotte&ts=1659566529385"; UD="LA=1659566529:CV=1659566529:TS=1659566529:SG=81eb9022bb235584be7202b852ab2d2c"; indeed_rcc="LV:CTK:UD"; jaSerpCount=1'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)