# “Permissions requested” dialog box not shown during onboarding to Cloud

_Applies to: Patch My PC Cloud_

### SYMPTOMS

I am trying to onboard an Intune tenant to Patch My PC (PMPC) Cloud.

However, after entering the credentials associated with the account used for my PMPC subscription, I don’t see the <strong>Permissions requested</strong> dialog box.\


![“Permissions requested” dialog box](/_images/image-(958).png "“Permissions requested” dialog box")

Instead, I’m just taken to the home page of the PMPC portal.\


![PMPC Portal home page](/_images/image-(960).png "PMPC Portal home page")

### CAUSE

There are two causes of this problem:

* An Intune administrator checked the optional <strong>Consent on behalf of your organization</strong> checkbox when they were prompted. By checking this box, that administrator has accepted the request to read the profile for all users in that tenant, negating the need to display the <strong>Permissions requested</strong> dialog box for other users.
* The Intune tenant has already been onboarded to the PMPC Cloud Platform. See the Resolution below if you need to reset it.

### RESOLUTION

To resolve this issue, check If the <strong>Patch My PC Cloud</strong> Enterprise Application is visible in the Azure Portal by following the [Deleting the Patch My PC Cloud application](../../cloud-administration/delete-the-patch-my-pc-cloud-enterprise-application.md) process.