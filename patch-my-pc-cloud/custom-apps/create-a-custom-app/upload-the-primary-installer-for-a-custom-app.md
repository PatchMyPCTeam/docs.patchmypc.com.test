# Upload the Primary Installer for a Custom App

_Applies to: Patch My PC Cloud Custom Apps_

To create a Custom App you first need up upload the Primary Installer for the app:

1. Sign in to the PMPC portal [https://portal.patchmypc.com/](https://portal.patchmypc.com/).
2.  On the **App Catalog** page, click **Add App**.\


    ![Clicking &#x22;Add App&#x22; on the App Catalog page](../../../_images/image%20%28209%29.png%20"Clicking%20&#x22;Add%20App&#x22;%20on%20the%20App%20Catalog%20page")

    \
    The Custom Apps Deployment Wizard starts.\


    ![Custom Apps Deployment Wizard](../../../_images/image%20%28210%29.png%20"Custom%20Apps%20Deployment%20Wizard")
3. On the **File** page, either:
   1. Click **Add Primary Install File** and browse to the location containing the app’s installer (EXE or MSI).
   2. Drag and drop the installer file onto this page.

{% hint style="danger" %}
**Important**

We currently do not support macOS Custom Apps. If you select a .pkg/.dmg you will see a warning stating this and explaining how you can upvote this idea.
{% endhint %}

![Clicking “Add Primary Install File” on the “Upload Application” page](../../../_images/image%20%28211%29.png%20"Clicking%20\"Add%20Primary%20Install%20File\"%20on%20the%20\"Upload%20Application\"%20page")

{% hint style="success" %}
**Tip**

If you plan to deploy an EXE-based installer, use our free script to help you extract the required information from the registry. See [Finding properties for EXE-Based Installers](../custom-apps-reference/find-properties-for-exe-based-installers.md) for more information.
{% endhint %}

The hash for the file is calculated as the file is uploaded to your portal and will show as **completed** once the file has been uploaded.

![Calculating the hash for the file as its uploaded to your portal.](../../../_images/image%20%28212%29.png%20"Calculating%20the%20hash%20for%20the%20file%20as%20its%20uploaded%20to%20your%20portal.")

4. If the installer does not require any additional folders or files, click **Next** to go to to the [General Information](custom-apps-general-information-tab.md) tab.\
   \
   If the installer does require additional folders or files, go to [Extra Folders and Files](custom-apps-file-tab.md).
