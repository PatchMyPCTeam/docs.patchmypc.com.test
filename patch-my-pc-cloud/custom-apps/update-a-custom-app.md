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

!\[]\(/\_images/image-(472 "").png "")

3. Click the app to open it.
4. On the app’s properties page, click **Add Version**.

!\[]\(/\_images/image-(473 "").png "")

The Custom Apps Deployment Wizard starts.

!\[]\(/\_images/image-(2636 "").png "")

5. On the **Add Version** page, either:
   1. Click **Add Primary Install File** and browse to the location containing the updated version of the app’s installer (EXE or MSI).
   2. Drag and drop the installer file onto this page.

!\[]\(/\_images/image-(2637 "").png "")

The hash for the file is calculated as the file is uploaded to your portal.

!\[]\(/\_images/image-(2638 "").png "")

6. If the installer does not require any additional files or folders, go to Step 8.
7. If the installer does require additional files or folders, either:
   1. Click the relevant **Add** button and browse to the location containing the additional files/folders.
   2. Drag and drop the files onto this page.

!\[]\(/\_images/image-(2639 "").png "")

{% hint style="info" %}
**Note**

If you choose to upload additional folders, you will be prompted to confirm you trust this site:

<img src="../../.gitbook/assets/image (2640).png" alt="Trust prompt" data-size="original">
{% endhint %}

8. Once the files/folders have uploaded, click **Next**.

!\[]\(/\_images/image-(2641 "").png "")

9. On the **Configuration** page, enter the version number and update any other fields as required.

{% hint style="info" %}
**Note**

If a Return Code defined in a Custom App has the same value but a different **Code type** to that defined in the deployment, the settings in the deployment take precedence.
{% endhint %}

!\[]\(/\_images/image-(2642 "").png "")

10. If you are happy you have entered all of the details for the app correctly, click **Save** otherwise, click **Next**.

!\[]\(/\_images/image-(2643 "").png "")

11. On the **Detection Rules** page, make any required changes.

!\[]\(/\_images/image-(2644 "").png "")

12. If you are happy you have entered all of the details for the app correctly, click **Save** otherwise, click **Next**.

!\[]\(/\_images/image-(2645 "").png "")

13. On the **Summary** page, review you have configured the app correctly.
    1. If you are happy, click **Create**.
    2. If you need to change something, click **< Prev** to backtrack through the Deployment Wizard to the relevant setting. Make the change, then step back through the wizard to this page. If everything is now correct, click **Create**.

!\[]\(/\_images/image-(2646 "").png "")

11. The App Catalog is displayed showing the version of the app along with the following notification:\
    \
    **Success Version <**_**version\_number**_**> has been successfully added to <**_**app\_name**_**>**.

!\[]\(/\_images/image-(483 "").png "") has been successfully added to \<app\_name>" width="563">

If the previous version of the app was deployed successfully, depending on the configured assignments, the new version will be installed the next time the daily sync runs.

Alternatively, you can use the [Sync Now](../cloud-deployments/manage-updates-in-cloud/sync-now-cloud-feature.md) process to update the app immediately without waiting for the next daily sync to run.
