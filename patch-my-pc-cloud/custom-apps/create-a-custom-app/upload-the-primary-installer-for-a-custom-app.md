# Upload the Primary Installer for a Custom App

_Applies to: Patch My PC Cloud Custom Apps_

To create a Custom App you first need up upload the Primary Installer for the app:

1. Sign in to the PMPC portal [https://portal.patchmypc.com/](https://portal.patchmypc.com/).
2.  On the **App Catalog** page, click **Add App**.\


    <figure><img src="../../../_images/gitbook/image (209).png" alt="Clicking &#x22;Add App&#x22; on the App Catalog page" width="563"><figcaption></figcaption></figure>

    \
    The Custom Apps Deployment Wizard starts.\


    <figure><img src="../../../_images/gitbook/image (210).png" alt="Custom Apps Deployment Wizard" width="563"><figcaption></figcaption></figure>
3. On the **File** page, either:
   1. Click **Add Primary Install File** and browse to the location containing the app’s installer (EXE or MSI).
   2. Drag and drop the installer file onto this page.

{% hint style="danger" %}
**Important**

We currently do not support macOS Custom Apps. If you select a .pkg/.dmg you will see a warning stating this and explaining how you can upvote this idea.
{% endhint %}

<figure><img src="../../../_images/gitbook/image (211).png" alt="Clicking “Add Primary Install File” on the “Upload Application” page " width="563"><figcaption></figcaption></figure>

{% hint style="success" %}
**Tip**

If you plan to deploy an EXE-based installer, use our free script to help you extract the required information from the registry. See [Finding properties for EXE-Based Installers](../custom-apps-reference/find-properties-for-exe-based-installers.md) for more information.
{% endhint %}

The hash for the file is calculated as the file is uploaded to your portal and will show as **completed** once the file has been uploaded.

<figure><img src="../../../_images/gitbook/image (212).png" alt="Calculating the hash for the file as its uploaded to your portal." width="563"><figcaption></figcaption></figure>

4. If the installer does not require any additional folders or files, click **Next** to go to to the [General Information](custom-apps-general-information-tab.md) tab.\
   \
   If the installer does require additional folders or files, go to [Extra Folders and Files](custom-apps-file-tab.md).
