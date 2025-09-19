# “Need admin approval” message when onboarding to Cloud

_Applies to: Patch My PC Cloud_

### SYMPTOMS

I am trying to onboard to Patch My PC (PMPC) Cloud. I’ve signed in, expecting to see the <strong>Permissions requested</strong> dialog box, but instead, I get the <strong>Need admin approval</strong> dialog box stating:

<strong>Patch My PC LLC needs permission to access resources in your organization that only an admin can grant. Please ask an admin to grant permission to this app before you can use it.</strong>\
\


![“Need admin approval” dialog box](/_images/image-(906).png "“Need admin approval” dialog box")

### CAUSE

This problem occurs because, as the message states, your Entra ID account is not a Global Administrator. As a result, you cannot consent to the PMPC Cloud application on your behalf.

### RESOLUTION

To resolve this issue, click <strong>Sign in with that account</strong> next to <strong>Have an admin account?</strong> and sign in with an admin account.

If you don't have a suitable admin account, contact the relevant person in your organization to obtain one or to perform the onboarding for you.