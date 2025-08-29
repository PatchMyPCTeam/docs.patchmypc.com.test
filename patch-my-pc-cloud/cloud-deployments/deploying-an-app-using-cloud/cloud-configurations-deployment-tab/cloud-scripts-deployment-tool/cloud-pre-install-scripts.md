# Cloud Pre-Install Scripts

_Applies to: Patch My PC Cloud_

A _Pre-Install Script_ is a script that can be run before the installer runs.

To add a Pre-Install script:

1. Click **Add** beside the **Pre-Install** option.

<figure><img src="/_images/gitbook/image%20%282605%29.png" alt="Clicking “Add” beside the “Pre-Install” option" width="419"><figcaption></figcaption></figure>

2. To import an existing script, click **Import** then browse to the location containing the script and select it.

<figure><img src="/_images/gitbook/image%20%282460%29.png" alt="Clicking “Import” to import an existing script" width="563"><figcaption></figcaption></figure>

The **Add Pre-Install Script** page is populated with the imported script.

<figure><img src="/_images/gitbook/image%20%282461%29.png" alt="The “Add Pre-Install Script” page is populated with the imported script." width="563"><figcaption></figcaption></figure>

3. To manually add a script, enter a unique name for the script in the **Script Name** field.

<figure><img src="/_images/gitbook/image%20%282462%29.png" alt="Entering a unique name for the script in the “Script Name” field" width="563"><figcaption></figcaption></figure>

4. Select the type of script from the **Script Format** dropdown.

<figure><img src="/_images/gitbook/image%20%282463%29.png" alt="Selecting the type of script from the “Script Format” dropdown." width="563"><figcaption></figcaption></figure>

5. In the script editor, type your script.

<figure><img src="/_images/gitbook/image%20%282464%29.png" alt="Typing your script in the Script Editor" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
**Note**

We currently have a limit of 50,000 characters per script. Use the **Number of characters used** counter to keep track of the number of characters you’ve entered in the script editor.
{% endhint %}

6.  In the **Arguments** field, enter any arguments you want to provide to the script.\


    <figure><img src="/_images/gitbook/image%20%282465%29.png" alt="Entering any arguments you want to provide to the script by specifying them in the “Arguments” field" width="563"><figcaption></figcaption></figure>

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


    <figure><img src="/_images/gitbook/image%20%282466%29.png" alt="Checking the “Don’t attempt software update if the pre script returns an exit code other than 0 or 3010” checkbox" width="563"><figcaption></figcaption></figure>


8.  Check the **Run the pre-update script before performing any auto-close or skip process checks** checkbox if you want to run the pre-install script before the conflicting process notification is displayed (if relevant).\
    \
    If you do not check this checkbox, we will run the pre-install script after the conflicting process notification.\


    <figure><img src="/_images/gitbook/image%20%282467%29.png" alt="	Checking the “Run the pre-update script before performing any auto-close or skip process checks” checkbox" width="563"><figcaption></figcaption></figure>
9.  Click **Save** to save your script.\


    <figure><img src="/_images/gitbook/image%20%282468%29.png" alt="" width="563"><figcaption></figcaption></figure>

    \
    The **Configurations** tab is re-displayed with the name of the configured script beside it.

<figure><img src="/_images/gitbook/image%20%2893%29.png" alt="“Configurations” tab re-displayed with the name of the configured script beside it" width="416"><figcaption></figcaption></figure>

{% hint style="success" %}
**Tip**

You can click **Edit** to edit a script or its settings. You can also click the red “`x`” beside a script to delete it.
{% endhint %}

***

If you do not want to configure any of the optional tabs under the **Tools** section, click **Next** to move to the [Assignments](../../cloud-assignments-deployment-tab.md) tab.

Otherwise, click on the relevant tab under **Tools** to configure the required settings, which are explained in the relevant article.
