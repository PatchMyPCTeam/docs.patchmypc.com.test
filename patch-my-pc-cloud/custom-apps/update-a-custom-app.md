# Update a Custom App

_Applies to: Custom Apps_

Once you have created and deployed a Custom App, you will probably need to update it at some point to a later version.

{% hint style="info" %}
Note

See [Modifying a Custom App](modify-a-custom-app.md) for details on how to make other changes to an existing Custom App.
{% endhint %}

To update a Custom App using Patch My PC (PMPC) Cloud:

1. Sign in to the PMPC portal [https://portal.patchmypc.com/](https://portal.patchmypc.com/).
2. On the **App Catalog** page, search for the relevant app.

![Searching for your Custom App](../../_images/image%20%28472%29.png%20"Searching%20for%20your%20Custom%20App")

3. Click the app to open it.
4. On the app’s properties page, click **Add Version**.

![Clicking “Add Version”](../../_images/image%20%28473%29.png%20"Clicking%20\"Add%20Version\"")

The Custom Apps Deployment Wizard starts.

![Custom Apps Deployment Wizard](../../_images/image%20%282636%29.png%20"Custom%20Apps%20Deployment%20Wizard")

5. On the **Add Version** page, either:
   1. Click **Add Primary Install File** and browse to the location containing the updated version of the app’s installer (EXE or MSI).
   2. Drag and drop the installer file onto this page.

![Clicking “Add Primary Install File” on the “Add Version” page](../../_images/image%20%282637%29.png%20"Clicking%20\"Add%20Primary%20Install%20File\"%20on%20the%20\"Add%20Version\"%20page")

The hash for the file is calculated as the file is uploaded to your portal.

![Calculating the hash for the file as its uploaded to your portal.](../../_images/image%20%282638%29.png%20"Calculating%20the%20hash%20for%20the%20file%20as%20its%20uploaded%20to%20your%20portal.")

6. If the installer does not require any additional files or folders, go to Step 8.
7. If the installer does require additional files or folders, either:
   1. Click the relevant **Add** button and browse to the location containing the additional files/folders.
   2. Drag and drop the files onto this page.

![Adding additional files or folders](../../_images/image%20%282639%29.png%20"Adding%20additional%20files%20or%20folders")

{% hint style="info" %}
**Note**

If you choose to upload additional folders, you will be prompted to confirm you trust this site:

![Trust prompt](../../_images/image%20%282640).png>)
{% endhint %}



8. Once the files/folders have uploaded, click **Next**.

![Clicking “Next”](../../_images/image%20%282641%29.png%20"Clicking%20\"Next\"")

9. On the **Configuration** page, enter the version number and update any other fields as required.

{% hint style="info" %}
**Note**

If a Return Code defined in a Custom App has the same value but a different **Code type** to that defined in the deployment, the settings in the deployment take precedence.
{% endhint %}

![Entering the version of the “Configuration page”](../../_images/image%20%282642%29.png%20"Entering%20the%20version%20of%20the%20\"Configuration%20page\"")

10. If you are happy you have entered all of the details for the app correctly, click **Save** otherwise, click **Next**.

![Clicking “Next”](../../_images/image%20%282643%29.png%20"Clicking%20\"Next\"")

11. On the **Detection Rules** page, make any required changes.

![Making any required changes on the &#x22;Detection Rules&#x22; page](../../_images/image%20%282644%29.png%20"Making%20any%20required%20changes%20on%20the%20&#x22;Detection%20Rules&#x22;%20page")

12. If you are happy you have entered all of the details for the app correctly, click **Save** otherwise, click **Next**.

![Clicking &#x22;Next&#x22;](../../_images/image%20%282645%29.png%20"Clicking%20&#x22;Next&#x22;")

13. On the **Summary** page, review you have configured the app correctly.
    1. If you are happy, click **Create**.
    2. If you need to change something, click **< Prev** to backtrack through the Deployment Wizard to the relevant setting. Make the change, then step back through the wizard to this page. If everything is now correct, click **Create**.

![Clicking “Save” on the “Summary” page](../../_images/image%20%282646%29.png%20"Clicking%20\"Save\"%20on%20the%20\"Summary\"%20page")

11. The App Catalog is displayed showing the version of the app along with the following notification:\
    \
    **Success Version <**_**version\_number**_**> has been successfully added to <**_**app\_name**_**>**.

![](../../_images/image%20%28483%29.png%20"")

If the previous version of the app was deployed successfully, depending on the configured assignments, the new version will be installed the next time the daily sync runs.

Alternatively, you can use the [Sync Now](../cloud-deployments/manage-updates-in-cloud/sync-now-cloud-feature.md) process to update the app immediately without waiting for the next daily sync to run.
