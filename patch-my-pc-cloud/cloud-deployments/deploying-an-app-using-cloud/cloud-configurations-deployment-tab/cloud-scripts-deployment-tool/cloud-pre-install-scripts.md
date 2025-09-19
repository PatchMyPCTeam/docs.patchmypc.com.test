# Cloud Pre-Install Scripts

_Applies to: Patch My PC Cloud_

A _Pre-Install Script_ is a script that can be run before the installer runs.

To add a Pre-Install script:

1. Click **Add** beside the **Pre-Install** option.

![Clicking “Add” beside the “Pre-Install” option](../../../../../.gitbook/assets/image-\(2605\).png)

2. To import an existing script, click **Import** then browse to the location containing the script and select it.

![Clicking “Import” to import an existing script](../../../../../.gitbook/assets/image-\(2460\).png)

The **Add Pre-Install Script** page is populated with the imported script.

![The “Add Pre-Install Script” page is populated with the imported script.](../../../../../.gitbook/assets/image-\(2461\).png)

3. To manually add a script, enter a unique name for the script in the **Script Name** field.

![Entering a unique name for the script in the “Script Name” field](../../../../../.gitbook/assets/image-\(2462\).png)

4. Select the type of script from the **Script Format** dropdown.

![Selecting the type of script from the “Script Format” dropdown.](../../../../../.gitbook/assets/image-\(2463\).png)

5. In the script editor, type your script.

![Typing your script in the Script Editor](../../../../../.gitbook/assets/image-\(2464\).png)

> **Note**
>
> We currently have a limit of 50,000 characters per script. Use the **Number of characters used** counter to keep track of the number of characters you’ve entered in the script editor.

6.  In the **Arguments** field, enter any arguments you want to provide to the script.\\

    ![Entering any arguments you want to provide to the script by specifying them in the “Arguments” field](../../../../../.gitbook/assets/image-\(2465\).png)

> **Tip**
>
> You can use variable names as arguments, provided they are enclosed by percentage signs (\`%\`). We provide common variables under this field, which you can add by clicking the plus (+) symbol or relevant variable name.

> **Important**
>
> Using script Arguments is currently unsupported when deploying an app to macOS.

7.  Check the **Don’t attempt software update if the pre script returns an exit code other than 0 or 3010** checkbox if you don’t want the app to be installed if the pre-script returns an exit code other than **0** or **3010**.\\

    If you do not check this checkbox, we will attempt to install the app regardless of the exit code returned by the pre-install script.\\

    ![Checking the “Don’t attempt software update if the pre script returns an exit code other than 0 or 3010” checkbox](../../../../../.gitbook/assets/image-\(2466\).png)
8.  Check the **Run the pre-update script before performing any auto-close or skip process checks** checkbox if you want to run the pre-install script before the conflicting process notification is displayed (if relevant).\
    \
    If you do not check this checkbox, we will run the pre-install script after the conflicting process notification.\\

    ![Checking the “Run the pre-update script before performing any auto-close or skip process checks” checkbox](../../../../../.gitbook/assets/image-\(2467\).png)
9.  Click **Save** to save your script.\\

    ![](../../../../../.gitbook/assets/image-\(2468\).png)

    \
    The **Configurations** tab is re-displayed with the name of the configured script beside it.

![“Configurations” tab re-displayed with the name of the configured script beside it](../../../../../.gitbook/assets/image-\(93\).png)

> **Tip**
>
> You can click **Edit** to edit a script or its settings. You can also click the red “\`x\`” beside a script to delete it.

**\***

**If you do not want to configure any of the optional tabs under the** Tools **section, click** Next **to move to the** [**Assignments**](../../cloud-assignments-deployment-tab.md) **tab.**

**Otherwise, click on the relevant tab under** Tools\*\* to configure the required settings, which are explained in the relevant article.
