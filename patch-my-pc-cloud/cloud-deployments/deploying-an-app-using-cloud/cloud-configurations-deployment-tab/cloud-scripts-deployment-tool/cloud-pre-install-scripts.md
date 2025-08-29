# Cloud Pre-Install Scripts

_Applies to: Patch My PC Cloud_

A _Pre-Install Script_ is a script that can be run before the installer runs.

To add a Pre-Install script:

1. Click **Add** beside the **Pre-Install** option.

![Clicking “Add” beside the “Pre-Install” option](../../../../../_images/image%20%282605%29.png%20"Clicking%20\"Add\"%20beside%20the%20\"Pre-Install\"%20option")

2. To import an existing script, click **Import** then browse to the location containing the script and select it.

![Clicking “Import” to import an existing script](../../../../../_images/image%20%282460%29.png%20"Clicking%20\"Import\"%20to%20import%20an%20existing%20script")

The **Add Pre-Install Script** page is populated with the imported script.

![The “Add Pre-Install Script” page is populated with the imported script.](../../../../../_images/image%20%282461%29.png%20"The%20\"Add%20Pre-Install%20Script\"%20page%20is%20populated%20with%20the%20imported%20script.")

3. To manually add a script, enter a unique name for the script in the **Script Name** field.

![Entering a unique name for the script in the “Script Name” field](../../../../../_images/image%20%282462%29.png%20"Entering%20a%20unique%20name%20for%20the%20script%20in%20the%20\"Script%20Name\"%20field")

4. Select the type of script from the **Script Format** dropdown.

![Selecting the type of script from the “Script Format” dropdown.](../../../../../_images/image%20%282463%29.png%20"Selecting%20the%20type%20of%20script%20from%20the%20\"Script%20Format\"%20dropdown.")

5. In the script editor, type your script.

![Typing your script in the Script Editor](../../../../../_images/image%20%282464%29.png%20"Typing%20your%20script%20in%20the%20Script%20Editor")

{% hint style="info" %}
**Note**

We currently have a limit of 50,000 characters per script. Use the **Number of characters used** counter to keep track of the number of characters you’ve entered in the script editor.
{% endhint %}

6.  In the **Arguments** field, enter any arguments you want to provide to the script.\


    ![Entering any arguments you want to provide to the script by specifying them in the “Arguments” field](../../../../../_images/image%20%282465%29.png%20"Entering%20any%20arguments%20you%20want%20to%20provide%20to%20the%20script%20by%20specifying%20them%20in%20the%20\"Arguments\"%20field")

{% hint style="success" %}
**Tip**

You can use variable names as arguments, provided they are enclosed by percentage signs (`%`). We provide common variables under this field, which you can add by clicking the plus (+) symbol or relevant variable name.
{% endhint %}

{% hint style="danger" %}
**Important**

Using script Arguments is currently unsupported when deploying an app to macOS.
{% endhint %}

7.  Check the **Don’t attempt software update if the pre script returns an exit code other than 0 or 3010** checkbox if you don’t want the app to be installed if the pre-script returns an exit code other than **0** or **3010**.\


    If you do not check this checkbox, we will attempt to install the app regardless of the exit code returned by the pre-install script.\


    ![Checking the “Don’t attempt software update if the pre script returns an exit code other than 0 or 3010” checkbox](../../../../../_images/image%20%282466%29.png%20"Checking%20the%20\"Don’t%20attempt%20software%20update%20if%20the%20pre%20script%20returns%20an%20exit%20code%20other%20than%200%20or%203010\"%20checkbox")


8.  Check the **Run the pre-update script before performing any auto-close or skip process checks** checkbox if you want to run the pre-install script before the conflicting process notification is displayed (if relevant).\
    \
    If you do not check this checkbox, we will run the pre-install script after the conflicting process notification.\


    ![Checking the “Run the pre-update script before performing any auto-close or skip process checks” checkbox](../../../../../_images/image%20%282467%29.png%20"Checking%20the%20\"Run%20the%20pre-update%20script%20before%20performing%20any%20auto-close%20or%20skip%20process%20checks\"%20checkbox")
9.  Click **Save** to save your script.\


    ![](../../../../../_images/image%20%282468%29.png%20"")

    \
    The **Configurations** tab is re-displayed with the name of the configured script beside it.

![“Configurations” tab re-displayed with the name of the configured script beside it](../../../../../_images/image%20%2893%29.png%20"\"Configurations\"%20tab%20re-displayed%20with%20the%20name%20of%20the%20configured%20script%20beside%20it")

{% hint style="success" %}
**Tip**

You can click **Edit** to edit a script or its settings. You can also click the red “`x`” beside a script to delete it.
{% endhint %}

***

If you do not want to configure any of the optional tabs under the **Tools** section, click **Next** to move to the [Assignments](../../cloud-assignments-deployment-tab.md) tab.

Otherwise, click on the relevant tab under **Tools** to configure the required settings, which are explained in the relevant article.
