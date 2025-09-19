# Configure a Default Cloud Deployment Template

_Applies to: Patch My PC Cloud_

The _Templates_ feature of Patch My PC (PMPC) Cloud allows you to optionally set one template per operating system (OS) platform as the default template to use whenever you create a deployment for that specific platform.

Once a default template has been configured, when you create a new deployment for that OS platform, the configuration settings defined in the template are automatically applied. You can still modify the settings if required.

You also apply a template to deployment as detailed in [Using Templates in Deployments](../../cloud-deployments/use-a-template-in-cloud-deployments.md).

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>If you previously set a default template but do not want to use it, see the [Unconfigure a Default Template](configure-a-default-cloud-deployment-template.md#unconfigure-a-default-template) section.</p>
<p>Also, configuring a default template for an OS platform does not affect any existing deployments to that platform. The default template will only apply to new deployments created after the default has been configured.</p>
</blockquote>

To configure the default template for all deployments to a specific OS platform:

1. Navigate to <strong>Settings | Templates</strong>

![Navigating to “Settings | Templates”](/_images/image-(261).png "Navigating to “Settings | Templates”")

2. On the <strong>Templates</strong> page, click the relevant slider under the <strong>Default</strong> column beside the template you want to configure as the default for all deployments created for that OS platform going forward.

![Clicking the “default” slider beside the relevant template](/_images/image-(47).png "Clicking the “default” slider beside the relevant template")

3. On the <strong>Are you sure you want to set ‘<</strong>_<strong>template\_name</strong>_<strong>>’ template as the default</strong> popup, click <strong>Yes</strong>.

![](/_images/image-(263).png "")

The <strong>Templates</strong> page is redisplayed, showing that the selected template is now the default template for all new deployments created for the relevant OS platform, along with the <strong>Success - Template “<</strong>_<strong>template\_name</strong>_<strong>>" successfully set as the default for <</strong>_<strong>platform</strong>_<strong>></strong> notification.

![](/_images/image-(49).png "")

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>You can only configure one template as the default per OS platform. If you want to choose a different template as the default, click the <strong>Default</strong> slider beside the relevant template and confirm you want to set that one as the default instead.</p>
</blockquote>

### Unconfigure a Default Template

If you have previously configured a default template but now do not want a default template to be applied to any new deployments:

1. Click the slider under the <strong>Default</strong> column beside the template you currently have configured as the default.

![Clicking the slider under the “Default” column beside the template currently configured as the default.](/_images/image-(51).png "Clicking the slider under the “Default” column beside the template currently configured as the default.")

2. On the A<strong>re you sure you want to unset ‘<</strong>_<strong>template\_name</strong>_<strong>>’ template as the default</strong> popup, click <strong>Yes</strong>.

![](/_images/image-(266).png "")

The <strong>Templates</strong> page is redisplayed, showing that the selected template is no longer the default template for all new deployments created for the relevant OS platform, along with the <strong>Success - Template “<</strong>_<strong>template\_name</strong>_<strong>>" successfully unset as the default for <</strong>_<strong>platform</strong>_<strong>></strong> notification.

![](/_images/image-(52).png "")