# Cloud Pre-Install Scripts

_Applies to: Patch My PC Cloud_

A _Pre-Install Script_ is a script that can be run before the installer runs.

To add a Pre-Install script:

1. Click **Add** beside the **Pre-Install** option.

![Clicking "Add" beside the "Pre-Install" option](/_images/image-(2605Add "Clicking \"Add\" beside the \"Pre-Install\" option").png "Clicking “Add” beside the “Pre-Install” option")

2. To import an existing script, click **Import** then browse to the location containing the script and select it.

![Clicking "Import" to import an existing script](/_images/image-(2460Import "Clicking \"Import\" to import an existing script").png "Clicking “Import” to import an existing script")

The **Add Pre-Install Script** page is populated with the imported script.

![The "Add Pre-Install Script" page is populated with the imported script.](/_images/image-(2461Add-Pre-Install-Script." "The \"Add Pre-Install Script\" page is populated with the imported script.").png "The “Add Pre-Install Script” page is populated with the imported script.")

3. To manually add a script, enter a unique name for the script in the **Script Name** field.

![Entering a unique name for the script in the "Script Name" field](/_images/image-(2462Script-Name "Entering a unique name for the script in the \"Script Name\" field").png "Entering a unique name for the script in the “Script Name” field")

4. Select the type of script from the **Script Format** dropdown.

![Selecting the type of script from the "Script Format" dropdown.](/_images/image-(2463Script-Format." "Selecting the type of script from the \"Script Format\" dropdown.").png "Selecting the type of script from the “Script Format” dropdown.")

5. In the script editor, type your script.

![Typing your script in the Script Editor](/_images/image-(2464 "Typing your script in the Script Editor").png "Typing your script in the Script Editor")

<blockquote class="wp-block-quote">
<p>**Note**</p>
<p>We currently have a limit of 50,000 characters per script. Use the **Number of characters used** counter to keep track of the number of characters you’ve entered in the script editor.</p>
</blockquote>

6.  In the **Arguments** field, enter any arguments you want to provide to the script.\


    ![Entering any arguments you want to provide to the script by specifying them in the "Arguments" field](/_images/image-(2465Arguments "Entering any arguments you want to provide to the script by specifying them in the \"Arguments\" field").png "Entering any arguments you want to provide to the script by specifying them in the “Arguments” field")

<blockquote class="wp-block-quote">
<p>**Tip**</p>
<p>You can use variable names as arguments, provided they are enclosed by percentage signs (`%`). We provide common variables under this field, which you can add by clicking the plus (+) symbol or relevant variable name.</p>
</blockquote>

<blockquote class="wp-block-quote">
<p>**Important**</p>
<p>Using script Arguments is currently unsupported when deploying an app to macOS.</p>
</blockquote>

7.  Check the **Don’t attempt software update if the pre script returns an exit code other than 0 or 3010** checkbox if you don’t want the app to be installed if the pre-script returns an exit code other than **0** or **3010**.\


    If you do not check this checkbox, we will attempt to install the app regardless of the exit code returned by the pre-install script.\


    ![Checking the "Don't attempt software update if the pre script returns an exit code other than 0 or 3010" checkbox](/_images/image-(2466Don-t-attempt-software-update-if-the-pre-script-returns-an-exit-code-other-than-0-or-3010 "Checking the \"Don't attempt software update if the pre script returns an exit code other than 0 or 3010\" checkbox").png "Checking the “Don’t attempt software update if the pre script returns an exit code other than 0 or 3010” checkbox")


8.  Check the **Run the pre-update script before performing any auto-close or skip process checks** checkbox if you want to run the pre-install script before the conflicting process notification is displayed (if relevant).\
    \
    If you do not check this checkbox, we will run the pre-install script after the conflicting process notification.\


    ![Checking the "Run the pre-update script before performing any auto-close or skip process checks" checkbox](/_images/image-(2467Run-the-pre-update-script-before-performing-any-auto-close-or-skip-process-checks "Checking the \"Run the pre-update script before performing any auto-close or skip process checks\" checkbox").png "Checking the “Run the pre-update script before performing any auto-close or skip process checks” checkbox")
9.  Click **Save** to save your script.\


    ![](/_images/image-(2468).png "")

    \
    The **Configurations** tab is re-displayed with the name of the configured script beside it.

!["Configurations" tab re-displayed with the name of the configured script beside it](/_images/image-(93Configurations "\"Configurations\" tab re-displayed with the name of the configured script beside it").png "“Configurations” tab re-displayed with the name of the configured script beside it")

<blockquote class="wp-block-quote">
<p>**Tip**</p>
<p>You can click **Edit** to edit a script or its settings. You can also click the red “`x`” beside a script to delete it.</p>
</blockquote>

***

If you do not want to configure any of the optional tabs under the **Tools** section, click **Next** to move to the [Assignments](../../cloud-assignments-deployment-tab.md) tab.

Otherwise, click on the relevant tab under **Tools** to configure the required settings, which are explained in the relevant article.