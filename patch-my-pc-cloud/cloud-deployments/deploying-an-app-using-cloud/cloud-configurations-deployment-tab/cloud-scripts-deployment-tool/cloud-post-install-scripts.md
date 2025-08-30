# Cloud Post-Install Scripts

_Applies to: Patch My PC Cloud_

A _Post-Install Script_ is a script that can be run after the installer runs.

To add a **Post-Install** script:

1. Click **Add** beside the **Post-Install** option.

![Clicking “Add” beside the “Post-Install” option](/_images/image-(2606).png "Clicking “Add” beside the “Post-Install” option")

2. To import an existing script, click **Import**, browse to the location containing the script, and select it.

![Clicking “Import” to import an existing script](/_images/image-(2450).png "Clicking “Import” to import an existing script")

The **Add Post-Install Script** page is populated with the imported script.

![“Add Post-Install Script” page is populated with the imported script.](/_images/image-(2451).png "“Add Post-Install Script” page is populated with the imported script.")

3. To manually add a script, enter a unique name for the script in the **Script Name** field.

![Entering a unique name for the script in the “Script Name” field](/_images/image-(2452).png "Entering a unique name for the script in the “Script Name” field")

4. Select the type of script from the **Script Format** dropdown.

![Selecting the type of script from the “Script Format” dropdown.](/_images/image-(2453).png "Selecting the type of script from the “Script Format” dropdown.")

5. In the script editor, type your script.

![Typing your script in the Script Editor](/_images/image-(2455).png "Typing your script in the Script Editor")

{% hint style="info" %}
**Note**

We currently have a limit of 50,000 characters per script. Use the **Number of characters used** counter to keep track of the number of characters you’ve entered in the script editor.
{% endhint %}

6.  In the **Arguments** field, enter any arguments you want to provide to the script.\


    ![Entering any arguments you want to provide to the script by specifying them in the “Arguments” field](/_images/image-(2456).png "Entering any arguments you want to provide to the script by specifying them in the “Arguments” field")

{% hint style="success" %}
**Tip**

You can use variable names as arguments, provided they are enclosed by percentage signs (`%`). We provide common variables under this field, which you can add by clicking the plus (`+`) symbol or relevant variable name.

&#x20;`%ReturnCode%` is currently only supported on post-scripts.
{% endhint %}

{% hint style="danger" %}
**Important**

Using script Arguments is currently unsupported when deploying an app to macOS.
{% endhint %}

7.  Click **Save** to save your script.\


    ![Clicking “Save” to save your script](/_images/image-(2457).png "Clicking “Save” to save your script")

    \
    The **Configurations** tab is re-displayed with the name of the configured script beside it.

![“Configurations” tab re-displayed with the name of the configured script beside it](/_images/image-(94).png "“Configurations” tab re-displayed with the name of the configured script beside it")

{% hint style="success" %}
**Tip**

You can click **Edit** to edit a script or its settings. You can also click the red “`x`” beside a script to delete it.
{% endhint %}

***

If you do not want to configure any of the optional tabs under the **Tools** section, click **Next** to move to the [Assignments](../../cloud-assignments-deployment-tab.md) tab.

Otherwise, click on the relevant tab under **Tools** to configure the required settings, which are explained in the relevant article.
