# Update a Binary Free App

_Applies to: Binary Free Apps for Patch My PC Cloud_

There are two ways to update the version of a Patch My PC (PMPC) Cloud Binary Free App:

* [From the update notification email](update-a-binary-free-app.md#update-a-binary-free-app-from-the-notification-email)
* [From the App Catalog](update-a-binary-free-app.md#update-a-binary-free-app-from-the-app-catalog)

### Update a Binary Free App from the Notification Email

If you have email notifications enabled for a Binary Free App, whenever we update the version in our App Catalog you will receive an email notification similar to the [Example Binary Free App Update Email](../cloud-reference/cloud-email-reference/example-binary-free-app-update-email.md).

To update the version of a Binary Free App from the notification email:

1.  Within the notification email, click **Update File**.\


    ![Clicking “Add Version” in the notification email](/_images/image-(401).png "Clicking “Add Version” in the notification email")


2.  If required, click **Sign In** on the new browser tab prompting you to sign in to your portal.\


    ![Clicking “Sign In” on the new browser tab prompting you to sign in to your portal.](/_images/image-(402).png "Clicking “Sign In” on the new browser tab prompting you to sign in to your portal.")


3.  Select the relevant account if you are already signed in or enter your credentials.\
    \
    The portal opens on the **“<**_**app\_name**_**>” Upload** file screen.\
    \


    ![](/_images/image-(403 "").png "")


4.  On the **Upload File Installer** screen, either:\
    a. Click **Select Application File** and browse to the location containing the app’s installer.

    b. Drag and drop the installer file onto this page.

{% hint style="success" %}
**Tip**

We suggest you use the download link at the bottom of the page to ensure you download the latest version of the app from the vendor’s official website.
{% endhint %}

![Clicking “Select Application File”](/_images/image-(404).png "Clicking “Select Application File”")

{% hint style="info" %}
**Note**

If you select either the wrong file or the wrong version of the file, the [Unable to verify the file you are trying to upload. Please ensure you have uploaded the correct file](../cloud-troubleshooting/troubleshooting-binary-free-apps/unable-to-verify-the-file-you-are-trying-to-upload-error-in-binary-free-apps.md) error will be displayed.

This is because we validate the hash of the installer to ensure you are uploading the correct file compared to the version information we have stored in our App Catalog.

If you really need to deploy an older version of the app, deploy it as a Custom App by using the [Create a Custom App](../custom-apps/create-a-custom-app/) process.
{% endhint %}

The hash for the file is calculated as the file is uploaded to your portal.

![Calculating the hash for the file as its uploaded to your portal](/_images/image-(405).png "Calculating the hash for the file as its uploaded to your portal")

The portal also shows **File Up to Date** and the **Success – File Successfully Uploaded** notification once:

* The file has been uploaded successfully.
* The calculated hash matches that stored in our App Catalog.

![“Success – File Successfully Uploaded” notification](/_images/image-(406).png "“Success – File Successfully Uploaded” notification")

You can now click **Back** or navigate to another area of the portal.

### Update a Binary Free App from the App Catalog

Whenever a new version of a Binary Free App is available in the App Catalog and we don’t have the latest installer file, the upload (![](/_images/image-(407 "").png>)) icon appears beside the app.

![“Upload” icon showing a new version of an app needs to be uploaded](/_images/image-(408).png "“Upload” icon showing a new version of an app needs to be uploaded")

To update a Binary Free App from the App Catalog:

1. Click the upload (![](/_images/image-(407 "").png>)) icon.
2.  On the app’s properties screen, click **Manage Files**.\


    ![Clicking “Manage Files”](/_images/image-(409).png "Clicking “Manage Files”")


3. Continue from Step 8 of the [Upload the app installer](deploy-a-binary-free-app.md#upload-the-app-installer) section of the [Create a Binary Free App](deploy-a-binary-free-app.md) process to upload the latest version.