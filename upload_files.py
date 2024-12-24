#!/usr/bin/python
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from os import listdir
arr = os.listdir()

gauth = GoogleAuth()           
drive = GoogleDrive(gauth)  

<OAuthV2 name="GenerateAccessToken">
    <Operation>GenerateAccessToken</Operation>
    <ExpiresIn>1800000</ExpiresIn> <!-- 30 minutes -->
    <RefreshTokenExpiresIn>17280000000</RefreshTokenExpiresIn> <!-- 200 days -->
    <SupportedGrantTypes>
      <GrantType>password</GrantType>
    </SupportedGrantTypes>
    <GenerateResponse enabled="true"/>
</OAuthV2>

for upload_file in arr:
        if upload_file.split('.')[1] == 'xlsx':
                gfile = drive.CreateFile({'parents': [{'id': '1xKdt047MmMv593'}]})
                gfile.SetContentFile(upload_file)
                gfile.Upload() # Upload the file.

a=os.listdir()
for i in a:
        if i.split('.')[1] == 'xlsx':
                os.remove(i);
                


