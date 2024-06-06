from dataclasses import dataclass


@dataclass(frozen=True)
class StringTools:
    """A collection of string manipulation tools."""

    # Strings for targeted sites
    site_urls = {
        'linked_in':'https://www.linkedin.com',
        'zip_recruiter': 'https://www.ziprecruiter.com/authn/login#intsrc=zr.fe.header_logged_out_homepage',
        'indeed' : 'https://secure.indeed.com/auth?hl=en_US&co=US&continue=https%3A%2F%2Fwww.indeed.com%2F&tmpl=desktop&from=gnav-util-homepage&jsContinue=https%3A%2F%2Fonboarding.indeed.com%2Fonboarding%3Fhl%3Den_US%26co%3DUS%26from%3Dgnav-homepage&empContinue=https%3A%2F%2Faccount.indeed.com%2Fmyaccess'
        }

    # Strings for LinkedIn
    li_search_strings = {
        'li_user_name_string':'session_key',
        'li_find_password_string':'session_password',
        'li_sign_in_button_string': '[data-id="sign-in-form__submit-btn"]',
        'li_find_job_type_string': '.search-global-typeahead__input',
        'li_find_job_list_continer_string':'.reusable-search__entity-result-list',
        'li_find_job_links':'a.app-aware-link'
        }

    # Strings for ZipRecruiter
    zr_search_strings = {
        'sign_in_button' : '.flex.h-full.flex-row.gap-12',
        'loggin_button' : '.flex-row',
        'login_input': 'email',
        'password_input': 'password',
        'submit_button': 'submit_button'
    }

    # Strings for Indeed
    id_search_strings = {}
