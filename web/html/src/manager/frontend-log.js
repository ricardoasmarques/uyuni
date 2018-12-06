/* eslint-disable */
"use strict";

const React = require("react");
const ReactDOM = require("react-dom");
const Loggerhead = require("loggerhead-module").create({ url: "/rhn/manager/frontend-log" });

const FrontendLog = React.createClass({
  componentWillMount: function() {
    Loggerhead.setHeaders = function(headers) {
      headers.set('X-CSRF-Token', document.getElementsByName('csrf_token')[0].value);
      return headers;
    }
    // store a log message about the error that just happened
    window.addEventListener('error', function(event) {
      // Note that col & error are new to the HTML 5 and may not be supported in every browser.
      var extra = !event.colno ? '' : '\ncolumn: ' + event.colno;
      extra += !event.error ? '' : '\nerror: ' + event.error;
      const errorMessage = event.message + '\nurl: ' + event.filename + '\nline: ' + event.lineno + extra;
      Loggerhead.error(errorMessage);
    });
  },

  render: function() {
    return null;
  }
});

ReactDOM.render(
  <FrontendLog />,
  document.getElementById('frontend-log')
);
