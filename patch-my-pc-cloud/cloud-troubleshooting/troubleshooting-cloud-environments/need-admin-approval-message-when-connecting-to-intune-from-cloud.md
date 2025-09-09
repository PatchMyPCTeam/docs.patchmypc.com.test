# “Need admin approval” message when connecting to Intune from Cloud

_Applies to: Intune Apps for Cloud_

### SYMPTOMS

I am trying to onboard to Intune Apps for Cloud (Intune Apps). I’ve signed in and clicked <strong>Connect</strong> to connect my Intune tenant, expecting to see the <strong>Permissions requested</strong> dialog box, but instead, I get the <strong>Need admin approval</strong> dialog box stating:

<strong>Patch My PC LLC needs permission to access resources in your organization that only an admin can grant. Please ask an admin to grant permission to this app before you can use it.</strong>\
\


![“Need admin approval” dialog box](/_images/image-(906).png "“Need admin approval” dialog box")

### CAUSE

This problem occurs because, as the message states, your Entra ID account is not a Global Administrator. As a result, you cannot consent to the PMPC Cloud application on your behalf.

### RESOLUTION

To resolve this issue, ensure you are completing this process using a <strong>Global Administrator</strong> account to create the enterprise app.