# Extra Files (Deployments)

_Applies to: Patch My PC Cloud_

{% hint style="info" %}
**Note**

Using the **Extra Files** tool is optional.
{% endhint %}

The **Extra Files** tool of the Patch My PC (PMPC) Cloud deployment wizard allows you to upload additional configuration files for a deployment.

To add extra folders and/or files:

1. Click the **Extra Files** tool to expose the configurable settings.

![Clicking the &#x22;Extra Files&#x22; tool](/_images/image-(82 "Clicking the &#x22;Extra Files&#x22; tool").png "Clicking the &#x22;Extra Files&#x22; tool")

2. Scroll down to the end of the **Extra Files** section so that the buttons and their subtext are visible.

![Scrolling down to the end of the &#x22;Extra Files&#x22; section so that the buttons and their subtext are visible](/_images/image-(83 "Scrolling down to the end of the &#x22;Extra Files&#x22; section so that the buttons and their subtext are visible").png "Scrolling down to the end of the &#x22;Extra Files&#x22; section so that the buttons and their subtext are visible")

3. Either:
   1. Drag and drop the relevant folders or files to the relevant area.
   2. Click the relevant button to browse to and select the relevant folders or files.

{% hint style="info" %}
**Note**

See [Unsupported File Names and Extensions for Extra Files](../../../cloud-reference/unsupported-file-names-and-extensions-in-cloud.md) for a list of filenames and extensions we do not support for upload.

Also, adding a folder will add any files and folders (including their files) within the selected folder.

We support uploading files with the same name, provided they are in different folders. We also support uploading folders with the same name, provided the selected paths are unique.
{% endhint %}

4.  Click **Upload** when your browser prompts you to upload the content.\
    \


    ![Clicking &#x22;Upload&#x22; when prompted to upload the content](/_images/image-(146 "Clicking &#x22;Upload&#x22; when prompted to upload the content").png "Clicking &#x22;Upload&#x22; when prompted to upload the content")

    \
    The hash will be calculated for any folders/files you upload, which will appear at the bottom of the **Extra Files** section.

![Additional folders/files to be uploaded appearing at the bottom of the “Extra Files” section](/_images/files-to-be-uploaded-appearing-at-the-bottom-of-the-Extra-Files-section "Additional folders/files to be uploaded appearing at the bottom of the “Extra Files” section")

{% hint style="info" %}
**Note**

The total number of extra folders/files is not limited, but their total size must not exceed the storage limits for your license type. See [Product Limitations](../../../cloud-product-limits.md)  for more details.

Also, if the **Installer Type** on the **General Information** page is set to **`.msi`**, the **MST File** section will be shown, allowing you to upload a single MST file. This file must have the **`.mst`** extension.

![“MST Files” section](/_images/image-(241 "“MST Files” section").png>)

Uploading a **`.mst`** file automatically adds the following to the **Additional Argument** field of the **Install Parameters** section:

**`TRANSFORMS=[<`**_**`mstfile>`**_**`].mst`**

where **`<`**_**`mstfile>`**_ is the name of the uploaded MST file.

![“Install Parameters” section updated](/_images/image-(243 "“Install Parameters” section updated").png>)
{% endhint %}

5. Repeat the above steps to add any additional folders/files as required.

{% hint style="info" %}
**Note**

Once a deployment has been successfully created, you can add or remove any additional folders or files as required.
{% endhint %}

6. If you do not want to configure any of the optional tabs under the **Tools** section, click **Next** to move to the [Assignments](../cloud-assignments-deployment-tab.md) tab.\
   \
   Otherwise, click on the relevant tab under **Tools** to configure the required settings, which are explained in the relevant process.

![Clicking &#x22;Next&#x22; to move to the &#x22;Assignments&#x22; page](/_images/image-(85 "Clicking &#x22;Next&#x22; to move to the &#x22;Assignments&#x22; page").png "Clicking &#x22;Next&#x22; to move to the &#x22;Assignments&#x22; page")

{% hint style="info" %}
**Note**

If you upload [Extra Files](extra-files-deployments.md) as part of your Patch My PC (PMPC) Cloud Deployment, you can reference those files in any of the [Scripts](cloud-scripts-deployment-tool/) in the same deployment by building a path relative to the script's current location. See [Referencing Extra Files in Scripts](../../cloud-deployments-reference/referencing-extra-files-in-scripts.md) for more information.
{% endhint %}
