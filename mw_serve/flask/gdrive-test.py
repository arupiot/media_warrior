from __future__ import print_function
from googleapiclient.discovery import build
from apiclient.http import MediaIoBaseDownload
import io
import sys
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/drive'
PATH = './test.mlp'

# and mimeType = 'application/vnd.google-apps.folder'

def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('drive', 'v3', http=creds.authorize(Http()))

    # Call the Drive v3 API
    # Will only work if the directory exists...
    results = service.files().list(
        pageSize=1, fields="nextPageToken, files(id, name)", q="name = 'mlp-samples-test' and mimeType = 'application/vnd.google-apps.folder'").execute()
    items = results.get('files', [])
    mlp_files_dir_id = None

    if not items:
        print('No MLP directory found.')
    else:
        print('Results from directory search (should be 1!):')
        for item in items:
            print('{0} ({1})'.format(item['name'], item['id']))
            mlp_files_dir_id = item['id']

    if mlp_files_dir_id is None:
      print('No mlp test dir found, exiting!')
      exit()

    results = service.files().list(pageSize=15, fields="nextPageToken, files(id, name)", q="'%s' in parents" % mlp_files_dir_id).execute()
    mlp_files_res = results.get('files', [])
    mlp_file_ids = None

    print ("Should be an array?")
    print (mlp_files_res)

    if not mlp_files_res:
        print('No MLP files found, exiting...')
        exit()
    else:
        print('MLP found:')
        for item in mlp_files_res:
            print('{0} ({1})'.format(item['name'], item['id']))
    
        # Download something...
        if (mlp_files_res): 
            for mlp_file in mlp_files_res: 
                file_id = mlp_file['id']
                request = service.files().get_media(fileId=file_id)
                fh = io.BytesIO()
                downloader = MediaIoBaseDownload(fh, request)
                done = False
                start = True
                print("Downloading %s..." % mlp_file['name'])
                while done is False and start is True:
                    status, done = downloader.next_chunk()
                    print(status.progress()*100.0)
                
                print ("Done")

                with open('./mlp_samples/' + mlp_file['name'],'wb') as out: ## Open temporary file as bytes
                    out.write(fh.getvalue()) 

                print (mlp_file['name'] + " written to disk!")
        else:
            print ("MLP dir not found!")
    
if __name__ == '__main__':
    main()