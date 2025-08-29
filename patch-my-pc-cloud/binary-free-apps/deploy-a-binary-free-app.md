# Deploy a Binary Free App

_Applies to: Binary Free Apps for Patch My PC Cloud_

There are two stages to deploying a Patch My PC (PMPC) Cloud Binary Free App:

* [Upload the app installer](deploy-a-binary-free-app.md#upload-the-app-installer)
* [Deploy the Binary Free app](deploy-a-binary-free-app.md#deploy-the-binary-free-app)

### Upload the app installer

To upload the app installer for the Binary Free App:

1. Download the relevant version of the software from the vendor for the app you wish to deploy.
2. Login to our portal.
3.  Search for the app in the **App Catalog**.\


    <figure><img src="../../_images/gitbook/image (443).png" alt="Searching for the app in the App Catalog"><figcaption></figcaption></figure>


4.  Click the app to open its properties.\


    <figure><img src="../../_images/gitbook/image (444).png" alt="Clicking the app to open its properties"><figcaption></figcaption></figure>

{% hint style="info" %}
**Note**

Notice that both the **Deploy** and **Edit Deployment** options are unavailable as this is a Binary Free App that requires you to upload the installer.
{% endhint %}

5.  Click **Manage Files**.\


    <figure><img src="../../_images/gitbook/image (445).png" alt="Clicking “Manage Files” "><figcaption></figcaption></figure>
6.  On the **“<**_**app\_name**_**>” Upload file** screen, click **Add App File**.\


    <figure><img src="../../_images/gitbook/image (446).png" alt="Clicking “Add App File”"><figcaption></figcaption></figure>


7.  On the **General Information** tab, configure the required options for the app, then click **Next**.\


    <figure><img src="../../_images/gitbook/image (447).png" alt="Configuring any required options for the app, then clicking “Next”"><figcaption></figcaption></figure>


8.  On the **Upload File Installer** tab, either:\
    \
    a. Click **Select Application File** and browse to the location containing the app’s installer.

    b. Drag and drop the installer file onto this page.

{% hint style="success" %}
**Tip**

We suggest you use the download link at the bottom of the page to ensure you download the latest version of the app from the vendor’s official website.
{% endhint %}

<figure><img src="../../_images/gitbook/image (448).png" alt="Clicking “Select Application File”"><figcaption></figcaption></figure>

{% hint style="info" %}
**Note**

If you select either the wrong file or the wrong version of the file, the [Unable to verify the file you are trying to upload. Please ensure you have uploaded the correct file](../cloud-troubleshooting/troubleshooting-binary-free-apps/unable-to-verify-the-file-you-are-trying-to-upload-error-in-binary-free-apps.md) error will be displayed.

This is because we validate the hash of the installer to ensure you are uploading the correct file compared to the version information we have stored in our App Catalog.

If you really need to deploy an older version of the app, deploy it as a Custom App by using the [Create a Custom App](../custom-apps/create-a-custom-app/)  process.
{% endhint %}

The hash for the file is calculated as the file is uploaded to your portal.

<figure><img src="../../_images/gitbook/image (2049).png" alt="Calculating the hash for the file as its uploaded to your portal."><figcaption></figcaption></figure>

The portal also shows **File Up to Date** and the **Success – File Successfully Uploaded** notification once:

* The file has been uploaded successfully.
*   The calculated hash matches that stored in our App Catalog.\


    <figure><img src="../../_images/gitbook/image (2050).png" alt="“Success – File Successfully Uploaded” notification "><figcaption></figcaption></figure>

{% hint style="info" %}
**Note**

By default, whenever a new version of a Binary Free App is released, we update the version in our App Catalog, which will trigger an update notification to be sent to all users configured in your portal.

See the [Manage New Version Notifications for a Binary Free App](manage-new-version-notifications-for-a-binary-free-app.md) process to change this.
{% endhint %}

### Deploy the Binary Free app

Once the app installer for the Binary Free App has been successfully uploaded, follow the [Deploy an App](../cloud-deployments/deploying-an-app-using-cloud/) process to deploy the app.
