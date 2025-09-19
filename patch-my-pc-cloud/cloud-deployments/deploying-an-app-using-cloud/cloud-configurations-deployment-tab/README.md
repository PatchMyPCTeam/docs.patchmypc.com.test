# Cloud "Configurations" Deployment tab

_Applies to: Patch My PC Cloud_

The **Configurations** tab of the Patch My PC (PMPC) Cloud deployment wizard allows you to configure various configuration settings (explained below) for how you want the app to be deployed.

<blockquote class="wp-block-quote">
<p>**Note**</p>
<p>The most common settings are displayed by default. You can configure additional, optional settings by clicking the relevant tab under the **Tools** section and following the relevant process.</p>
<p>If any configuration options mentioned below are missing from your deployment, it is probably because the specific feature(s) the option relates to have not been enabled in your PMPC Cloud company.</p>
<p>Any settings you configure for a deployment will be used for the current deployment and automatically applied to any new versions of the deployment as it's updated.</p>
</blockquote>

This tab contains the following settings:

* [Apply Template](./#apply-template)
*
  [Built-in Auto Updates](./#built-in-auto-updates)
* [Desktop Shortcut](./#desktop-shortcut)
* [Available Uninstall](./#available-uninstall)
* [Conflicting Process](./#conflicting-process)
* [Conflicting Process - Settings](./#conflicting-process-settings)
* [Notify Timeout Configuration](./#notify-timeout-configuration)
* [Notification Policy](./#notification-policy)
* [Conflicting Process - Conflicting Process](./#conflicting-process-conflicting-process)

!["Configurations" tab](/_images/image-(2601 '"Configurations" tab').png "&#x22;Configurations&#x22; tab")

### **Apply Template**

Allows you to apply a [Template](../../use-a-template-in-cloud-deployments.md) of pre-configured settings to this deployment.

### **Built-in Auto Updates**

| Option               | Description                                                                                                                                                                                                                                                                                                                                        |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Disable Self-Updates | <p>If an app supports built-in auto-updates, this option will be shown and enabled by default, disabling any auto-updates.</p><p></p><p>There might be apps that have built-in auto-updates, but do not support controlling this setting by setting an install parameter or a registry value. In such cases, 
this option will be unavailable.</p> |

### **Desktop Shortcut**

| Option                  | Description                                                                           |
| ----------------------- | ------------------------------------------------------------------------------------- |
| Remove Desktop Shortcut | If checked, will remove the desktop shortcut created as part of the app installation. |

### **Available Uninstall**

| Option                    | Description                                                                             |
| ------------------------- | --------------------------------------------------------------------------------------- |
| Allow Available Uninstall | If checked, allows Intune Apps to uninstall the app if the Company Portal installed it. |

### **Conflicting Process**

The installation of some apps cannot be completed if the app:

* is currently running
* uses a shared process that needs to be closed, but in doing so, could impact that process and other apps using it.

This setting lets you manage those conflicting processes (also known as "_Conflicting Process_"), and control what happens in such scenarios using one of the following options.

| Option                                                         | Description                                                                                                                                                                                                                                                                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Perform the installation                                       | Performs the installation regardless.                                                                                                                                                                                                                                                                          |
| Auto-close conflicting application process before installation | <p>Automatically closes the app/process causing the conflict to allow this app to be installed.<br><br><mark style="color:red;"><strong>IMPORTANT</strong></mark><br>This can result in data loss so use with care.</p>                                                                                        |
| Skip installation when conflicting processes are in use        | <p>The installation is skipped until the conflicting process is no longer in use.<br><br><mark style="color:blue;"><strong>NOTE</strong></mark><br>If the user snoozes/defers the update, Intune reports the installation as a failure and retries 24 hours later.</p>                                         |
| Notify the user to close the application                       | <p>The default option.<br><br>The user sees a notification requesting they close the app that is preventing this install.<br><br><mark style="color:blue;"><strong>NOTE</strong></mark><br>If the user snoozes/defers the update, Intune reports the installation as a failure and retries 24 hours later.</p> |

### Conflicting Process - Settings

Allows you to configure the following **Advanced Settings** for Conflicting Processes.

### **Notify Timeout Configuration**

How long in seconds (**300** by default), before the notification timeouts.

### **Notification Policy**

| Option                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Notification behavior if the application running and focus assist is enabled | <p>How the notification behaves if the app is currently running and Focus Assist is enabled:<br><br>o Discard the Notification (default)<br>o Always show the notification<br>o Show the notification if the deferred policy is reached</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Do not allow user deferral                                                   | The user cannot defer the installation. The app will close and update when the timeout expires.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Allow the user to defer the installation                                     | <p>When an installation is postponed, Intune interprets the installation as a failure and automatically retries it 24 hours later.</p><p></p><p>Using this option, the user can defer the installation:</p><p></p><p>o <strong>Indefinitely –</strong> If selected, Intune will retry the installation forever, giving the user the option to postpone it every 24 hours.</p><p></p><p>o <strong>Up to X times -</strong> The user can postpone the installation the configured number of times with a 24-hour gap between retries. Intune will retry the installation every 24 hours until the user has no more deferrals. At this point the conflicting process will be closed and the update will be installed.</p><p></p><p>o <strong>First notification displayed –</strong> With this option, the user will get the first notification about the conflicting process after the number of days configured. However, even though Intune will retry the installation every 24 hours, the retries will be automatically postponed again until the number of configured days pass. Only then will the user get the conflicting process notification again.</p> |
| Prevent the application from being opened while it is updating               | <p>Prevents the app from opening whilst it is being updated.<br><br><mark style="color:blue;"><strong>NOTE</strong></mark><br>See the <a href="https://patchmypc.com/kb/manage-conflicting-processes-when-updating/#h-update-in-progress">Update in progress</a> section of <a href="https://patchmypc.com/kb/manage-conflicting-processes-when-updating/">Manage Conflicting Processes when Updating Third-Party Applications</a> for more information about this option.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

### Conflicting Process - Conflicting Process

Clicking the **Conflicting Process** button lets you see any conflicting processes we have identified that will prevent an app from updating.

You can also add additional entries or remove existing entries to suit your environment.

***

If you do not want to configure any of the optional tabs under the **Tools** section, click **Next** to move to the [Assignments](../cloud-assignments-deployment-tab.md) tab.

Otherwise, click on the relevant tab under **Tools** to configure the required settings, which are explained in the relevant process.

![Clicking "Next" to move to the "Assignments" tab](/_images/image-(2602 'Clicking "Next" to move to the "Assignments" tab').png "Clicking &#x22;Next&#x22; to move to the &#x22;Assignments&#x22; tab")