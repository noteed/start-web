using System.Net;
using Microsoft.AspNetCore.Mvc;
using Newtonsoft.Json.Linq;
using RazorEngine;
using RazorEngine.Templating;

namespace app.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class HelloController : ControllerBase
    {

        [HttpGet]
        [Route("/hello/1")]
        public ContentResult Get() {
            string html = @"
<html>
<head></head>
<body>
<code><pre>
Hello/1.

This response is hard-coded in `HelloController.cs`.


Back to <a href=""/"">index</a>.
</pre></code>
</body>
</html>
";

            return new ContentResult {
                ContentType = "text/html",
                StatusCode = (int)HttpStatusCode.OK,
                Content = html
            };
        }

        [HttpGet]
        [Route("/hello/{value}")]
        public ContentResult Get(int value) {
            var dict = new { value = value }; 
            var json = JObject.FromObject(dict);

            string template = System.IO.File.ReadAllText("templates/hello.html");
            string html = Engine.Razor.RunCompile(template, "key", null, json);

            return new ContentResult {
                ContentType = "text/html",
                StatusCode = (int)HttpStatusCode.OK,
                Content = html
            };
        }

    }
}
