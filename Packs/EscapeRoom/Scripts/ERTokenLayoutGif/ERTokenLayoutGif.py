import demistomock as demisto
from CommonServerPython import *

import traceback


def set_indicator_hint(indicator_id):
    res = demisto.executeCommand('setIndicator', {
        'id': indicator_id,
        'customFields': {
            'userpswdhint': ' ',
        },
    })

    if is_error(res):
        demisto.error(f'oylo!\n{res}\n\n')


''' MAIN FUNCTION '''


def main():
    args = demisto.args()
    try:
        indicator_id = dict_safe_get(args, ['indicator', 'id'])
        set_indicator_hint(indicator_id)
        return_results(
            CommandResults(readable_output='![](https://media.giphy.com/media/5vR6pNsjhoKwo/giphy.gif)')
        )
    except Exception as exc:
        demisto.error(traceback.format_exc())  # print the traceback
        return_error(f'Failed to execute ERTokenLayoutGif. Error: {str(exc)}')


''' ENTRY POINT '''

if __name__ in ('__main__', '__builtin__', 'builtins'):
    main()