# Browser Crashes when uploading a large number of files using the Cloud portal

_Applies to: Patch My PC Cloud_

### SYMPTOMS

I have a folder named "**MyFolder**" that contains 3,000 files, totaling 3GB. This folder needs to be available in the cache folder alongside the installer during installation.

However, when I try uploading these files to a Custom App or as Extra Files for a deployment using the Patch My PC (PMPC) portal, my browser crashes.

### CAUSE

When too many concurrent worker operations occur during file uploads to either Custom Apps or even as Extra Files for a deployment, the browser's performance is significantly impacted, leading to freezing and eventual crashing.

This is due to inherent limitations and is not related to the PMPC Cloud Portal but rather to browser performance constraints.

To mitigate this, PMPC has limited the number of files that can be uploaded at once to 1,000.

If you try to upload more than 1000 files at once, the upload will fail with the error message

> You have selected too many files (available: 1000)

![](/_images/image%20%282600%29.png "")

### RESOLUTION

If you need to upload more than 1,000 files in one go, we recommend using the following workaround to compress them into a ZIP file and upload just this ZIP file as an Extra File.

Then, when you deploy the app, you can configure a Pre-Installation script using the example below to extract the files.

#### Example Scenario

Consider the scenario mentioned above, where you have a folder named "**MyFolder**" containing 3,000 files totaling 3GB. This folder should be available in the cache folder alongside the installer during installation.

{% hint style="info" %}
**Note**

If your scenario differs from the above, you should adjust the example scripts, ensuring you thoroughly test them. We provide no support for them or accept any liability for their use, which you do at your own risk.

Please test these scripts thoroughly outside of the PMPC portal to ensure they work as expected before using them in your instance of the portal.
{% endhint %}

#### Step 1: Compress the Folder into a ZIP File

Use the following PowerShell script to create a ZIP file. In this example, the folder to be compressed is located at **C:\Temp\MyFolder**

`Define the path to the folder you want to compress`\
`$sourceFolderPath = "C:\temp\MyFolder"`\
`Define the path where the zip archive should be created`\
`$zipFilePath = "C:\Temp\MyFolder.zip"`\
`Create the zip archive`\
`Compress-Archive -Path $sourceFolderPath -DestinationPath $zipFilePath -Force -ErrorAction 'Stop'`

After running this script, a file named **C:\Temp\MyFolder.zip** will be created.

#### Step 2: Upload the ZIP Archive

Create your Custom App or upload the ZIP archive as an **Extra File** in a deployment.

![Adding the “MyFolder.zip” as an Extra File](/_images/image%20%282381%29.png "Adding the \"MyFolder.zip\" as an Extra File")

#### Step 3: Extract the ZIP Archive During Deployment

During the app deployment step, specify a script to extract the ZIP archive in the same folder. The script below uses the **$PSScriptRoot** automatic variable to determine the correct extraction path.

{% hint style="info" %}
**Note**

**$PSScriptRoot** is an automatic variable in PowerShell that represents the folder where the script is located. This ensures the ZIP file is extracted in the same location as the installation files.
{% endhint %}

`# Define the path to the zip file`\
`$zipFilePath = Join-Path -Path $PSScriptRoot -ChildPath 'MyFolder.zip'`\
`# Define the destination path`\
`$destinationPath = $PSScriptRoot`\
`# Extract the ZIP archive`\
`Expand-Archive -Path $zipFilePath -DestinationPath $destinationPath -Force -ErrorAction 'Stop'`

#### Step 4: Upload the Extraction Script as a Pre-Install Script

Upload the extraction script as a Pre-Install Script in your deployment settings.

![Uploading the extraction script as a Pre-Install Script in your deployment settings](/_images/image%20%282382%29.png "Uploading the extraction script as a Pre-Install Script in your deployment settings")

#### Step 5: Create the Deployment and Test

1. Finalize your deployment configuration.
2. Test the deployment on a few machines before rolling it out to production.

By following these steps, you can successfully upload and deploy apps containing a large number of files without encountering browser crashes.
