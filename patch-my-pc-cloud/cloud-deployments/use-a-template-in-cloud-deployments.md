# Use a Template in Cloud Deployments

_Applies to: Patch My PC Cloud_

Once the _Deployment Templates_ ([_Templates_](../cloud-administration/manage-cloud-deployment-templates/)) feature of Patch My PC (PMPC) Cloud has been enabled for your PMPC Cloud company and you have created at least one template, you can start using templates for your new deployments.

{% hint style="info" %}
**Note**

Templates are currently unsupported for use in existing deployments. To configure an existing deployment to use a template, you need to delete it and recreate a new one. When creating the new deployment, you can choose which template to use.

Also, if a template contains an option that is not supported by a deployment, that option will not be shown in the portal.

If a template contains an option that is supported by a deployment, that option will be shown in the portal with its configuration set as per the template. However, you can modify the configuration of that option if required.
{% endhint %}

To configure a new deployment to use a template:

1. Follow the relevant deployment scenario.
2.  Once the Deployment Wizard has started, click **Apply Template**\\

    ![Clicking “Apply Template”](<../../.gitbook/assets/image-(2330) (1).png>)

{% hint style="info" %}
**Note**

You can click **Apply Template** at any time, regardless of the tab you are working on.
{% endhint %}

3.  On the **Apply Template** screen, select the radio button beside the template you want to apply, then click **Apply**.\\

    ![Selecting the radio button beside the template you want to apply and clicking “Apply”](<../../.gitbook/assets/image-(2331) (1).png>)

{% hint style="info" %}
**Note**

Only the templates created for the Operating System (OS) platform you are deploying to are shown.
{% endhint %}

The Deployment Wizard is redisplayed along with the **Success - Template ‘<**_**template\_name**_**>’ applied** notification.

![](../../.gitbook/assets/image-\(2332\).png)

{% hint style="info" %}
**Note**

You can click **Apply Template** again to select and re-apply a template (which overwrites any existing settings) at any time before you click **Deploy** to ensure the template settings are applied to this deployment.
{% endhint %}
