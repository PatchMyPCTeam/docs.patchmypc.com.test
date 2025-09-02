# Cloud Post-Uninstall Script

_Applies to: Patch My PC Cloud_

A _Post-Uninstall Script_ is a script that can be run after the uninstaller runs.

To add a Post-Uninstall script:

1. Click **Add** beside the **Post-Uninstall** option.

![Clicking “Add” beside the “Post-Uninstall” option](/_images/image-(2608 "Clicking “Add” beside the “Post-Uninstall” option").png "Clicking “Add” beside the “Post-Uninstall” option")

2. To import an existing script, click **Import** then browse to the location containing the script and select it.

![Clicking “Import” to import an existing script](/_images/image-(2473 "Clicking “Import” to import an existing script").png "Clicking “Import” to import an existing script")

The **Add Post-Uninstall Scripts** page is populated with the imported script.

![“Add Post-Uninstall Script” page is populated with the imported script.](/_images/image-(2474 "“Add Post-Uninstall Script” page is populated with the imported script.").png "“Add Post-Uninstall Script” page is populated with the imported script.")

3. To manually add a script, enter a unique name for the script in the **Script Name** field.

![Entering a unique name for the script in the “Script Name” field](/_images/image-(2475 "Entering a unique name for the script in the “Script Name” field").png "Entering a unique name for the script in the “Script Name” field")

4. Select the type of script from the **Script Format** dropdown.

![Selecting the type of script from the “Script Format” dropdown.](/_images/image-(2476 "Selecting the type of script from the “Script Format” dropdown.").png "Selecting the type of script from the “Script Format” dropdown.")

5. In the script editor, type your script.

![Typing your script in the Script Editor](/_images/image-(2477 "Typing your script in the Script Editor").png "Typing your script in the Script Editor")

{% hint style="info" %}
**Note**

We currently have a limit of 50,000 characters per script. Use the **Number of characters used** counter to keep track of the number of characters you’ve entered in the script editor.
{% endhint %}

6.  In the **Arguments** field, enter any arguments you want to provide to the script.\


    ![Entering any arguments you want to provide to the script by specifying them in the “Arguments” field](/_images/image-(2478 "Entering any arguments you want to provide to the script by specifying them in the “Arguments” field").png "Entering any arguments you want to provide to the script by specifying them in the “Arguments” field")

{% hint style="success" %}
**Tip**

You can use variable names as arguments, provided they are enclosed by percentage signs (`%`). We provide common variables under this field, which you can add by clicking the plus (`+`) symbol or relevant variable name.

`%ReturnCode%` is currently only supported on post-scripts.
{% endhint %}

{% hint style="danger" %}
**Important**

Using script Arguments is currently unsupported when deploying an app to macOS.
{% endhint %}

7.  Click **Save** to save your script.\


    ![Clicking “Save” to save your script](/_images/image-(2479 "Clicking “Save” to save your script").png "Clicking “Save” to save your script")

    \
    The **Configurations** tab is re-displayed with the name of the configured script beside it.

![“Configurations” tab re-displayed with the name of the configured script beside it](/_images/image-(96 "“Configurations” tab re-displayed with the name of the configured script beside it").png "“Configurations” tab re-displayed with the name of the configured script beside it")

{% hint style="success" %}
**Tip**

You can click **Edit** to edit a script or its settings. You can also click the red “`x`” beside a script to delete it.
{% endhint %}

***

If you do not want to configure any of the optional tabs under the **Tools** section, click **Next** to move to the [Assignments](../../cloud-assignments-deployment-tab.md) tab.

Otherwise, click on the relevant tab under **Tools** to configure the required settings, which are explained in the relevant article.
