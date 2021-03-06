# Copyright (c) 2020 SUSE LLC
# Licensed under the terms of the MIT license.

@sle12sp4_ssh_minion
Feature: Bootstrap a SLES 12 SP4 Salt SSH Minion

  Scenario: Clean up sumaform leftovers on a SLES 12 SP4 Salt SSH Minion
    When I perform a full salt minion cleanup on "sle12sp4_ssh_minion"

  Scenario: Bootstrap a SLES 12 SP4 system managed via salt-ssh
    Given I am authorized
    And I go to the bootstrapping page
    Then I should see a "Bootstrap Minions" text
    And I check "manageWithSSH"
    And I enter the hostname of "sle12sp4_ssh_minion" as "hostname"
    And I enter "linux" as "password"
    And I select "1-sle12sp4_ssh_minion_key" from "activationKeys"
    And I select the hostname of "proxy" from "proxies"
    And I click on "Bootstrap"
    Then I wait until I see "Successfully bootstrapped host!" text
    And I wait until onboarding is completed for "sle12sp4_ssh_minion"

# WORKAROUD for bsc#1124634
# Package 'sle-manager-tools-release' is automatically installed during bootstrap and
# stays installed after removal of channel containing it. So it is not possible to update it.
# Package needs to be removed from highstate to avoid failure when updating it.
  Scenario: Remove sle-manager-tools-release from state after SLES 12 SP4 bootstrap
    Given I am on the Systems overview page of this "sle12sp4_ssh_minion"
    When I remove package "sle-manager-tools-release" from highstate

# WORKAROUD for bsc#1178328
  Scenario: Install dmidecode package to avoid a Hardware Refresh issue in SLES 12 SP4 SSH minion
    And I install package "dmidecode" on this "sle12sp4_ssh_minion"

@proxy
  Scenario: Check connection from SLES 12 SP4 SSH minion to proxy
    Given I am on the Systems overview page of this "sle12sp4_ssh_minion"
    When I follow "Details" in the content area
    And I follow "Connection" in the content area
    Then I should see "proxy" short hostname

@proxy
  Scenario: Check registration on proxy of SLES 12 SP4 SSH minion
    Given I am on the Systems overview page of this "proxy"
    When I follow "Details" in the content area
    And I follow "Proxy" in the content area
    Then I should see "sle12sp4_ssh_minion" hostname

  Scenario: Schedule errata refresh to reflect channel assignment on SLES 12 SP4 SSH minion
    Given I am authorized as "admin" with password "admin"
    When I follow the left menu "Admin > Task Schedules"
    And I follow "errata-cache-default"
    And I follow "errata-cache-bunch"
    And I click on "Single Run Schedule"
    Then I should see a "bunch was scheduled" text
    And I wait until the table contains "FINISHED" or "SKIPPED" followed by "FINISHED" in its first rows

  Scenario: Check events history for failures on SLES 12 SP4 SSH minion
    Given I am on the Systems overview page of this "sle12sp4_ssh_minion"
    Then I check for failed events on history event page
