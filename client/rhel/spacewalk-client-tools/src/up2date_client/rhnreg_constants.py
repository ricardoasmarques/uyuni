# -*- coding: utf-8 -*-
#
# String constants for the RHN Register TUI/GUI.
# Copyright (c) 2000--2016 Red Hat, Inc.
#
# Author:
#       James Slagle <jslagle@redhat.com>


from up2date_client.pmPlugin import PM_PLUGIN_NAME, PM_NAME

import gettext
t = gettext.translation('rhn-client-tools', fallback=True)
# Python 3 translations don't have a ugettext method
if not hasattr(t, 'ugettext'):
    t.ugettext = t.gettext
_ = t.ugettext

PRODUCT_NAME          = _("Uyuni")

COPYRIGHT_TEXT        = _(u"Copyright © 2006--2014 Red Hat, Inc. All rights reserved.")

# Satellite URL Window
SATELLITE_URL_WINDOW  = _("Enter your {PRODUCT_NAME} URL.").format(PRODUCT_NAME=PRODUCT_NAME)
SATELLITE_URL_TEXT    = _("Please enter the location of your {PRODUCT_NAME} "
                          "server and of its SSL "
                          "certificate. The SSL certificate is only required "
                          "if you will be connecting over https (recommended).").format(PRODUCT_NAME=PRODUCT_NAME)
SATELLITE_URL_PROMPT  = _("{PRODUCT_NAME} URL:").format(PRODUCT_NAME=PRODUCT_NAME)
SATELLITE_URL_PROMPT2 = _("SSL certificate:")
SATELLITE_REQUIRED    = _("You must enter a valid {PRODUCT_NAME} URL.").format(PRODUCT_NAME=PRODUCT_NAME)
SSL_REQUIRED          = _("If you are using https you must enter the location "
                          "of a valid SSL certificate.")

# Connect Window
CONNECT_WINDOW        = _("Attempting to contact the Spacewalk server.")
CONNECT_WINDOW_TEXT   = _("We are attempting to contact the {PRODUCT_NAME} "
                          "server at %s.").format(PRODUCT_NAME=PRODUCT_NAME)
CONNECT_WINDOW_TEXT2  = _("A proxy was specified at %s.")

# Start Window
START_REGISTER_WINDOW = _("System Registration")
START_REGISTER_TEXT   = _("This assistant will guide you through "
                          "connecting your system to "
                          "{PRODUCT_NAME} to receive software "
                          "updates, including "
                          "security updates, to keep your system supported "
                          "and compliant.  "
                          "You will need the following at this time:\n\n"
                          " * A network connection\n"
                          " * Your {PRODUCT_NAME} Login & password\n"
                          " * The location of a {PRODUCT_NAME} Server "
                          "or Proxy\n\n").format(PRODUCT_NAME=PRODUCT_NAME)

# Why Register Window
WHY_REGISTER          = _("Why Should I Connect to {PRODUCT_NAME}? ...").format(PRODUCT_NAME=PRODUCT_NAME)
WHY_REGISTER_WINDOW   = _("Why Register")
WHY_REGISTER_TEXT     = _("Connecting your system to {PRODUCT_NAME} allows you to take full "
                          "advantage of the benefits of a paid subscription, including:").format(PRODUCT_NAME=PRODUCT_NAME)
WHY_REGISTER_SEC      = _("Security & Updates:")
WHY_REGISTER_DLD      = _("Downloads & Upgrades:")
WHY_REGISTER_SUPP     = _("Support:")
WHY_REGISTER_COMP     = _("Compliance:")
WHY_REGISTER_SEC_TXT  = _("Receive the latest software updates, including security updates, keeping this "
                          "system updated and secure.")
WHY_REGISTER_DLD_TXT  = _("Download installation images for system releases, "
                          "including new releases.")
WHY_REGISTER_SUPP_TXT = _("Access to the technical support experts for help "
                          "with any issues you might encounter with this system.")
WHY_REGISTER_COMP_TXT = _("Stay in compliance with your subscription agreement "
                          "and manage subscriptions "
                          "for systems connected to your account.")
WHY_REGISTER_TIP      = _("Tip: SUSE values your privacy: "
                          "https://www.suse.com/company/legal/")
BACK_REGISTER         = _("Take me back to the registration")

# Confirm Quit Window
CONFIRM_QUIT           = _("Software Update Not Set Up")
CONFIRM_QUIT_SURE       = _("Are you sure you don't want to connect your system to {PRODUCT_NAME}? "
                           "You'll miss out on the benefits of a SLES/RHEL subscription:\n").format(PRODUCT_NAME=PRODUCT_NAME)
CONFIRM_QUIT_WILLNOT       = _("You will not be able to take advantage of these subscription privileges without connecting "
                           "your system to {PRODUCT_NAME}.\n").format(PRODUCT_NAME=PRODUCT_NAME)
CONTINUE_REGISTERING   = _("Take me back to the setup process.")
REGISTER_LATER2        = _("I'll register later.")

# Info Window
REGISTER_WINDOW   = _("{PRODUCT_NAME} Account").format(PRODUCT_NAME=PRODUCT_NAME)
LOGIN_PROMPT      = _("Please enter your login information for the %s {PRODUCT_NAME}:\n\n").format(PRODUCT_NAME=PRODUCT_NAME)
HOSTED_LOGIN      = _("{PRODUCT_NAME} Login:").format(PRODUCT_NAME=PRODUCT_NAME)
LOGIN             = _("Login:")
PASSWORD          = _("Password:")
LOGIN_TIP         = _("Tip: Forgot your login or password?  Contact your "
                      "{PRODUCT_NAME} Organization Administrator.").format(PRODUCT_NAME=PRODUCT_NAME)
USER_REQUIRED     = _("Please enter a desired login.")
PASSWORD_REQUIRED = _("Please enter and verify a password.")

# OS Release Window
SELECT_OSRELEASE             = _("Operating System Release Version")
OS_VERSION                   = _("Operating System version:")
MINOR_RELEASE                = _(" Minor Release: ")
LIMITED_UPDATES              = _("Limited Updates Only")
ALL_UPDATES                  = _("All available updates")
CONFIRM_OS_RELEASE_SELECTION = _("Confirm operating system release selection")
CONFIRM_OS_ALL               = _("Your system will be subscribed to the base"
                                 " software channel to receive all available"
                                 " updates.")

# Hardware Window
HARDWARE_WINDOW = _("Create Profile - Hardware")
HARDWARE_WINDOW_DESC1 = _("A Profile Name is a descriptive name that"
                          " you choose to identify this System Profile"
                          " on the {PRODUCT_NAME} web pages. Optionally,"
                          " include a computer serial or identification number.").format(PRODUCT_NAME=PRODUCT_NAME)
HARDWARE_WINDOW_DESC2 = _("Additional hardware information including PCI"
                          " devices, disk sizes and mount points will be"
                          " included in the profile.")
HARDWARE_WINDOW_CHECKBOX = _("Include the following information about hardware"
                             " and network:")

# Packages Window
PACKAGES_WINDOW         = _("Create Profile - Packages")
PACKAGES_WINDOW_DESC1   = _("RPM information is important to determine what"
                          " updated software packages are relevant to this"
                          " system.")
PACKAGES_WINDOW_DESC2   = _("Include RPM packages installed on this system"
                          " in my System Profile")
PACKAGES_WINDOW_UNCHECK = _("You may deselect individual packages by"
                            " unchecking them below.")
PACKAGES_WINDOW_PKGLIST = _("Building Package List")

# Product Window
EMAIL                  = _("*Email Address:")

SYSTEM_ALREADY_SETUP = _("System Already Registered")
SYSTEM_ALREADY_REGISTERED = _("It appears this system has already been set up for software updates:")
SYSTEM_ALREADY_REGISTERED_CONT = _("Are you sure you would like to continue?")

RHSM_SYSTEM_ALREADY_REGISTERED = _("This system has already been registered using Red Hat Subscription Management.\n\n"
                                "Your system is being registered again using Red Hat Satellite"
                                " or Red Hat Satellite Proxy technology. Red Hat recommends that customers only register once.\n\n"
                                "To learn more about RHN Classic/Red Hat Satellite registration and technologies please consult this"
                                " Knowledge Base Article: https://access.redhat.com/kb/docs/DOC-45563")

# Send Window
SEND_WINDOW      = _("Send Profile Information to {PRODUCT_NAME}").format(PRODUCT_NAME=PRODUCT_NAME)
SEND_WINDOW_DESC = _("We are finished collecting information for the System Profile.\n\n"
                     "Press \"Next\" to send this System Profile to {PRODUCT_NAME}.  "
                     "Click \"Cancel\" and no information will be sent.  "
                     "You can run the registration program later by "
                     "typing `rhn_register` at the command line.").format(PRODUCT_NAME=PRODUCT_NAME)

# Sending Window
SENDING_WINDOW = _("Sending Profile to {PRODUCT_NAME}").format(PRODUCT_NAME=PRODUCT_NAME)

# Finish Window
FINISH_WINDOW           = _("Updates Configured")
FINISH_WINDOW_TEXT_TUI  = _("You may now run '%s update' from this system's "
                            "command line to get the latest "
                            "software updates from {PRODUCT_NAME}. You will need to run this "
                            "periodically to "
                            "get the latest updates. Alternatively, you may configure this "
                            "system for automatic software updates (also known as 'auto errata update') "
                            "via the {PRODUCT_NAME} web interface. (Instructions for this are in the {PRODUCT_NAME} Reference "
                            "Guide, available from the 'Help' button in the main {PRODUCT_NAME} "
                            "web interface.)").format(PRODUCT_NAME=PRODUCT_NAME) % PM_NAME

# Review Window
REVIEW_WINDOW           = _("Review Subscription")
REVIEW_WINDOW_PROMPT    = _("Please review the subscription details below:")
SUB_NUM                 = _("The installation number %s was activated during "
                            "this system's initial connection to {PRODUCT_NAME}.").format(PRODUCT_NAME=PRODUCT_NAME)
SUB_NUM_RESULT          = _("Subscriptions have been activated for the following "
                            "products/services:")
CHANNELS_TITLE          = _("Software Channel Subscriptions:")
OK_CHANNELS             = _("This system will receive updates from the "
                            "following software channels:")
CHANNELS_SAT_WARNING    = _("Warning: Only installed product listed above will receive "
                            "updates and support. If you would like "
                            "to receive updates for additional products, please "
                            "login to your {PRODUCT_NAME} web interface "
                            "and subscribe this system to the appropriate "
                            "software channels.").format(PRODUCT_NAME=PRODUCT_NAME)
PM_PLUGIN_WARNING       = _("Warning: %s is not present, could not enable it.\n"
                            "Automatic updates will not work.") % (PM_PLUGIN_NAME)
PM_PLUGIN_CONF_CHANGED  = _("Note: %s has been enabled.") % (PM_PLUGIN_NAME)
PM_PLUGIN_CONF_ERROR    = _("Warning: An error occurred during enabling %s.\n"
                            "%s is not enabled.\n"
                            "Automatic updates will not work.") % (PM_PLUGIN_NAME, PM_PLUGIN_NAME)
FAILED_CHANNELS         = _("You were unable to be subscribed to the following "
                            "software channels because there were insufficient "
                            "subscriptions available in your account:")
NO_BASE_CHANNEL            = _(
"This system was unable to subscribe to any software channels. Your system "
"will not receive any software updates to keep it secure and supported. "
"Contact your {PRODUCT_NAME} administrator about this problem. Once you make the "
"appropriate active subscriptions available in your account, you may browse "
"to this system's profile in the {PRODUCT_NAME} web interface and subscribe this system "
"to software channels via the software > software channels tab.").format(PRODUCT_NAME=PRODUCT_NAME)
SLOTS_TITLE             = _("Service Level:")
OK_SLOTS                = _("Depending on what {PRODUCT_NAME} system types are associated with a system, you'll "
                            "enjoy different benefits. The following are the "
                            "{PRODUCT_NAME} system types associated with this system:").format(PRODUCT_NAME=PRODUCT_NAME)
SLOTS                   =  SLOTS_TITLE + "\n" + OK_SLOTS + "\n%s"
FAILED_SLOTS            = _("This system was unable to be associated with the "
                            "following {PRODUCT_NAME} system type(s) because there were "
                            "insufficient subscriptions available in your account:").format(PRODUCT_NAME=PRODUCT_NAME)
MANAGEMENT              = _("Management type: automatic updates, systems "
                            "grouping, systems permissions, system package profiling, "
                            "bare-metal provisioning, existing state provisioning, "
                            "rollbacks, configuration management")

VIRT = _("Virtualization type: software updates for a limited number of "
        "virtual guests on this system.")


VIRT_FAILED = _("<b>Warning:</b> Any guest systems you create on this system "
        "and register to {PRODUCT_NAME} will consume system "
        "subscriptions beyond this host system's subscription. You will need "
        "to: (1) make a virtualization system entitlement available and "
        "(2) apply that system entitlement to this "
        "system in {PRODUCT_NAME} web interface if you do not want virtual guests of "
        "this system to consume additional subscriptions.").format(PRODUCT_NAME=PRODUCT_NAME)

NO_SYS_ENTITLEMENT         = _("This system was unable to be associated with "
"any {PRODUCT_NAME} system types. This system will not receive any software "
"updates to keep it secure and supported. Contace your {PRODUCT_NAME} administrator "
"about this problem. Once you make the "
"appropriate active subscriptions available in your account, you may browse "
"to this system's profile in the {PRODUCT_NAME} web interface, delete the profile, and "
"re-connect this system to {PRODUCT_NAME}.").format(PRODUCT_NAME=PRODUCT_NAME)
ACTIVATION_KEY          = _("Universal default activation key detected\n"
                            "A universal default activation key was detected in your account. "
                            "This means that a set of properties (software channel subscriptions, "
                            "package installations, system group memberships, etc.) "
                            "for your system's connection to {PRODUCT_NAME} Server or {PRODUCT_NAME} Proxy"
                            "have been determined by the activation key rather than your "
                            "installation number.  "
                            "You may also refer to the {PRODUCT_NAME} Reference Guide for more details "
                            "about activation keys. \n"
                            "Universal Default activation key: %s").format(PRODUCT_NAME=PRODUCT_NAME)

# Error Messages.
FATAL_ERROR                = _("Fatal Error")
WARNING                    = _("Warning")
HOSTED_CONNECTION_ERROR    = _("We can't contact {PRODUCT_NAME}.\n\n"
                               "Double check the location provided - is '%s' correct?\n"
                               "If not, you can correct it and try again.\n\n"
                               "Make sure that the network connection on this system is operational.\n\n"
                               "This system will not be able to successfully receive software updates "
                               "without connecting to an {PRODUCT_NAME} server/proxy").format(PRODUCT_NAME=PRODUCT_NAME)

BASECHANNELERROR           = _("Architecture: %s, OS Release: %s, OS "
                               "Version: %s")
SERVER_TOO_OLD             = _("This server doesn't support functionality "
                               "needed by this version of the software update"
                               " setup client. Please try again with a newer "
                               "server.")


SSL_CERT_ERROR_MSG         = _("<b><span size=\"16000\">Incompatible Certificate File</span></b>\n\n"
                               "The certificate you provided, <b>%s</b>, is not compatible with "
                               " the {PRODUCT_NAME} server at <b>%s</b>. You may want to double-check"
                               " that you have provided a valid certificate file."
                               " Are you sure you have provided the correct certificate, and that"
                               " the certificate file has not been corrupted?\n\n"
                               "Please try again with a different certificate file.").format(PRODUCT_NAME=PRODUCT_NAME)

SSL_CERT_EXPIRED           = _("<b><span size=\"12000\">Incompatible Certificate File</span></b>\n\n"
                               " The certificate is expired. Please ensure you have the correct "
                               " certificate and your system time is correct.")

SSL_CERT_FILE_NOT_FOUND_ERRER = _("Please verify the values of sslCACert and serverURL in "
                                  "/etc/sysconfig/rhn/up2date. You can either make the "
                                  "serverURL use http instead of https, or you can "
                                  "download the SSL cert from your {PRODUCT_NAME}, place it "
                                  "in /usr/share/rhn, and ensure sslCACert points to it.").format(PRODUCT_NAME=PRODUCT_NAME)

ACT_KEY_USAGE_LIMIT_ERROR = _("Problem registering system.\n\n"
                              "A universal default activation key limits the "
                              "number of systems which can connect to "
                              "the {PRODUCT_NAME} organization associated with your "
                              "login. To allow this system to connect, "
                              "please contact your {PRODUCT_NAME} organization "
                              "administrator to increase the number of "
                              "systems allowed to connect or to disable "
                              "this universal default activation key.").format(PRODUCT_NAME=PRODUCT_NAME)

CHANNEL_PAGE_TIP       = _("\n Tip: Minor releases with a '*' are currently"
                           " supported by Red Hat.\n\n")

CHANNEL_PAGE_WARNING = _("Warning:You will not be able to limit this"
                          " system to minor release that is older than"
                          " the recent minor release if you select this"
                          " option.\n")

CONFIRM_OS_WARNING      = _("Your system will be subscribed to %s \n"
                            "base software channel. You will not be\n"
                            "able to move this system to an earlier release\n"
                            "(you will be able to move to a newer release).\n"
                            "Are you sure you would like to continue?")



# Navigation
OK        = _("OK")
ERROR     = _("Error")
NEXT      = _("Next")
BACK      = _("Back")
CANCEL    = _("Cancel")
NO_CANCEL = _("No, Cancel")
YES_CONT  = _("Yes, Continue")
DESELECT  = _("Press <space> to deselect the option.")


