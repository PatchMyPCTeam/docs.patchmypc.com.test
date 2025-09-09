# Update a Custom App

_Applies to: Custom Apps_

Once you have created and deployed a Custom App, you will probably need to update it at some point to a later version.

<blockquote class="wp-block-quote">
<p>Note</p>
<p>See [Modifying a Custom App](modify-a-custom-app.md) for details on how to make other changes to an existing Custom App.</p>
</blockquote>

To update a Custom App using Patch My PC (PMPC) Cloud:

1. Sign in to the PMPC portal [https://portal.patchmypc.com/](https://portal.patchmypc.com/).
2. On the <strong>App Catalog</strong> page, search for the relevant app.

![Searching for your Custom App](/_images/image-(472).png "Searching for your Custom App")

3. Click the app to open it.
4. On the app’s properties page, click <strong>Add Version</strong>.

![Clicking “Add Version”](/_images/image-(473).png "Clicking “Add Version”")

The Custom Apps Deployment Wizard starts.

![Custom Apps Deployment Wizard](/_images/image-(2636).png "Custom Apps Deployment Wizard")

5. On the <strong>Add Version</strong> page, either:
   1. Click <strong>Add Primary Install File</strong> and browse to the location containing the updated version of the app’s installer (EXE or MSI).
   2. Drag and drop the installer file onto this page.

![Clicking “Add Primary Install File” on the “Add Version” page](/_images/image-(2637).png "Clicking “Add Primary Install File” on the “Add Version” page")

The hash for the file is calculated as the file is uploaded to your portal.

![Calculating the hash for the file as its uploaded to your portal.](/_images/image-(2638).png "Calculating the hash for the file as its uploaded to your portal.")

6. If the installer does not require any additional files or folders, go to Step 8.
7. If the installer does require additional files or folders, either:
   1. Click the relevant <strong>Add</strong> button and browse to the location containing the additional files/folders.
   2. Drag and drop the files onto this page.

![Adding additional files or folders](/_images/image-(2639).png "Adding additional files or folders")

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>If you choose to upload additional folders, you will be prompted to confirm you trust this site:</p>
<p>![Trust prompt](/_images/image (2640).png>)</p>
</blockquote>



8. Once the files/folders have uploaded, click <strong>Next</strong>.

![Clicking “Next”](/_images/image-(2641).png "Clicking “Next”")

9. On the <strong>Configuration</strong> page, enter the version number and update any other fields as required.

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>If a Return Code defined in a Custom App has the same value but a different <strong>Code type</strong> to that defined in the deployment, the settings in the deployment take precedence.</p>
</blockquote>

![Entering the version of the “Configuration page”](/_images/image-(2642).png "Entering the version of the “Configuration page”")

10. If you are happy you have entered all of the details for the app correctly, click <strong>Save</strong> otherwise, click <strong>Next</strong>.

![Clicking “Next”](/_images/image-(2643).png "Clicking “Next”")

11. On the <strong>Detection Rules</strong> page, make any required changes.

![Making any required changes on the &#x22;Detection Rules&#x22; page](/_images/image-(2644).png "Making any required changes on the &#x22;Detection Rules&#x22; page")

12. If you are happy you have entered all of the details for the app correctly, click <strong>Save</strong> otherwise, click <strong>Next</strong>.

![Clicking &#x22;Next&#x22;](/_images/image-(2645).png "Clicking &#x22;Next&#x22;")

13. On the <strong>Summary</strong> page, review you have configured the app correctly.
    1. If you are happy, click <strong>Create</strong>.
    2. If you need to change something, click <strong>< Prev</strong> to backtrack through the Deployment Wizard to the relevant setting. Make the change, then step back through the wizard to this page. If everything is now correct, click <strong>Create</strong>.

![Clicking “Save” on the “Summary” page](/_images/image-(2646).png "Clicking “Save” on the “Summary” page")

11. The App Catalog is displayed showing the version of the app along with the following notification:\
    \
    <strong>Success Version <</strong>_<strong>version\_number</strong>_<strong>> has been successfully added to <</strong>_<strong>app\_name</strong>_<strong>></strong>.

![](/_images/image-(483).png "")

If the previous version of the app was deployed successfully, depending on the configured assignments, the new version will be installed the next time the daily sync runs.

Alternatively, you can use the [Sync Now](../cloud-deployments/manage-updates-in-cloud/sync-now-cloud-feature.md) process to update the app immediately without waiting for the next daily sync to run.