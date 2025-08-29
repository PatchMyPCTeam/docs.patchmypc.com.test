# Cloud Post-Install Scripts

_Applies to: Patch My PC Cloud_

A _Post-Install Script_ is a script that can be run after the installer runs.

To add a **Post-Install** script:

1. Click **Add** beside the **Post-Install** option.

<figure><img src="/_images/gitbook/image%20%282606%29.png" alt="Clicking “Add” beside the “Post-Install” option" width="419"><figcaption></figcaption></figure>

2. To import an existing script, click **Import**, browse to the location containing the script, and select it.

<figure><img src="/_images/gitbook/image%20%282450%29.png" alt="Clicking “Import” to import an existing script" width="563"><figcaption></figcaption></figure>

The **Add Post-Install Script** page is populated with the imported script.

<figure><img src="/_images/gitbook/image%20%282451%29.png" alt="“Add Post-Install Script” page is populated with the imported script." width="563"><figcaption></figcaption></figure>

3. To manually add a script, enter a unique name for the script in the **Script Name** field.

<figure><img src="/_images/gitbook/image%20%282452%29.png" alt="Entering a unique name for the script in the “Script Name” field" width="563"><figcaption></figcaption></figure>

4. Select the type of script from the **Script Format** dropdown.

<figure><img src="/_images/gitbook/image%20%282453%29.png" alt="Selecting the type of script from the “Script Format” dropdown." width="563"><figcaption></figcaption></figure>

5. In the script editor, type your script.

<figure><img src="/_images/gitbook/image%20%282455%29.png" alt="Typing your script in the Script Editor" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
**Note**

We currently have a limit of 50,000 characters per script. Use the **Number of characters used** counter to keep track of the number of characters you’ve entered in the script editor.
{% endhint %}

6.  In the **Arguments** field, enter any arguments you want to provide to the script.\


    <figure><img src="/_images/gitbook/image%20%282456%29.png" alt="Entering any arguments you want to provide to the script by specifying them in the “Arguments” field" width="563"><figcaption></figcaption></figure>

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


    <figure><img src="/_images/gitbook/image%20%282457%29.png" alt="Clicking “Save” to save your script" width="563"><figcaption></figcaption></figure>

    \
    The **Configurations** tab is re-displayed with the name of the configured script beside it.

<figure><img src="/_images/gitbook/image%20%2894%29.png" alt="“Configurations” tab re-displayed with the name of the configured script beside it" width="418"><figcaption></figcaption></figure>

{% hint style="success" %}
**Tip**

You can click **Edit** to edit a script or its settings. You can also click the red “`x`” beside a script to delete it.
{% endhint %}

***

If you do not want to configure any of the optional tabs under the **Tools** section, click **Next** to move to the [Assignments](../../cloud-assignments-deployment-tab.md) tab.

Otherwise, click on the relevant tab under **Tools** to configure the required settings, which are explained in the relevant article.
