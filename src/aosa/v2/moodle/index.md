---
title: "Moodle"
template: "page"
---

*by Tim Hunt*

Moodle is a web application used in educational settings. While this chapter will try to give an overview of all aspects of how Moodle works, it focuses on those areas where Moodle's design is particularly interesting:

- The way the application is divided into plugins;

- The permission system, which controls which users can perform which actions in different parts of the system;

- The way output is generated, so that different themes (skins) can be used to give different appearances, and so that the interface can be localised.

- The database abstraction layer.

Moodle[^1] provides a place online where students and teachers can come together to teach and learn. A Moodle site is divided into *courses*. A course has *users* enrolled in it with different roles, such as *Student* or *Teacher*. Each course comprises a number of *resources* and *activities*. A resource might be a PDF file, a page of HTML within Moodle, or a link to something elsewhere on the web. An activity might be a forum, a quiz or a wiki. Within the course, these resources and activities will be structured in some way. For example they may be grouped into logical topics, or into weeks on a calendar.

![Figure 1: Moodle course](course.png)

Moodle can be used as a standalone application. Should you wish to teach courses on software architecture (for example) you could download Moodle to your web host, install it, start creating courses, and wait for students to come and self-register. Alternatively, if you are a large institution, Moodle would be just one of the systems you run. You would probably also have the infrastructure shown in Figure 2.

![Figure 2: Typical university systems architecture](university.png)

- An authentication/identity provider (for example LDAP) to control user accounts across all your systems.

- A student information system; that is, a database of all your students, which program of study they are on, and hence which courses they need to complete; and their transcript---a high-level summary of the results of the courses they have completed. This would also deal with other administrative functions, like tracking whether they have paid their fees.

- A document repository (for example, Alfresco); to store files, and track workflow as users collaborate to create files.

- An ePortfolio; this is a place where students can assemble assets, either to build a CV (resume), or to provide evidence that they have met the requirements of a practice-based course.

- A reporting or analytics tool; to generate high-level information about what is going on in your institution.

Moodle focuses on providing an online space for teaching and learning, rather than any of the other systems that an educational organisation might need. Moodle provides a basic implementation of the other functionalities, so that it can function either as a stand-alone system or integrated with other systems. The role Moodle plays is normally called a virtual learning environment (VLE), or learning or course management system (LMS, CMS or even LCMS).

Moodle is open source or free software (GPL). It is written in PHP. It will run on most common web servers, on common platforms. It requires a database, and will work with MySQL, PostgreSQL, Microsoft SQL Server or Oracle.

The Moodle project was started by Martin Dougiamas in 1999, while he was working at Curtin University, Australia. Version 1.0 was released in 2002, at which time PHP4.2 and MySQL 3.23 were the technologies available. This limited the kind of architecture that was possible initially, but much has changed since then. The current release is the Moodle 2.2.x series.

## An Overview of How Moodle Works

A Moodle installation comprises three parts:

1.  The code, typically in a folder like `/var/www/moodle` or `~``/htdocs/moodle`. This should not be writable by the web server.

2.  The database, managed by one of the supported RDMSs. In fact, Moodle adds a prefix to all the table names, so it can share a database with other applications if desired.

3.  The `moodledata` folder. This is a folder where Moodle stores uploaded and generated files, and so needs to be writable by the web server. For security reasons, the should be outside the web root.

These can all be on a single server. Alternatively, in a load-balanced set-up, there will be multiple copies of the code on each web server, but just one shared copy of the database and `moodledata`, probably on other servers.

The configuration information about these three parts is stored in a file called `config.php` in the root of the `moodle` folder when Moodle is installed.

### Request Dispatching

Moodle is a web applications, so users interact with it using their web browser. From Moodle's point of view that means responding to HTTP requests. An important aspect of Moodle's design is, therefore, the URL namespace, and how URLs get dispatched to different scripts.

Moodle uses the standard PHP approach to this. To view the main page for a course, the URL would be `.../course/view.php?id=123`, where `123` is the unique id of the course in the database. To view a forum discussion, the URL would be something like `.../mod/forum/discuss.php?id=456789`. That is, these particular scripts, `course/view.php` or `mod/forum/discuss.php`, would handle these requests.

This is simple for the developer. To understand how Moodle handles a particular request, you look at the URL and start reading code there. It is ugly from the user's point of view. These URLs are, however, permanent. The URLs do not change if the course is renamed, or if a moderator moves a discussion to a different forum.[^2]

The alternative approach one could take is to have a single entry point `…/index.php/[extra­information-to-make-the-request-unique]`. The single script `index.php` would then dispatch the requests in some way. This approach adds a layer of indirection, which is something software developers always like to do. The lack of this layer of indirection does not seem to hurt Moodle.

### Plugins

Like many successful open source projects, Moodle is built out of many plugins, working together with the core of the system. This is a good approach because at allows people to change and enhance Moodle in defined ways. An important advantage of an open source system is that you can tailor it to your particular needs. Making extensive customisations to the code can, however, lead to big problems when the time comes to upgrade, even when using a good version control system. By allowing as many customisations and new features as possible to be implemented as self-contained plugins that interact with the Moodle core through a defined API, it is easier for people to customise Moodle to their needs, and to share customisations, while still being able to upgrade the core Moodle system.

There are various ways a system can be built as a core surrounded by plugins. Moodle has a relatively fat core, and the plugins are strongly-typed. When I say a fat core, I mean that there is a lot of functionality in the core. This contrasts with the kind of architecture where just about everything, except for a small plugin-loader stub, is a plugin.

When I say plugins are strongly typed, I mean that depending on which type of functionality you want to implement, you have to write a different type of plugin, and implement a different API. For example, a new Activity module plugin would be very different from a new Authentication plugin or a new Question type. At the last count there are about 35 different types of plugin[^3]. This contrasts with the kind of architecture where all plugins use basically the same API and then, perhaps, subscribe to the subset of hooks or events they are interested in.

Generally, the trend in Moodle has been to try to shrink the core, by moving more functionality into plugins. This effort has only been somewhat successful, however, because an increasing feature-set tends to expand the core. The other trend has been to try to standardise the different types of plugin as much as possible, so that in areas of common functionality, like install and upgrade, all types of plugins work the same way.

A plugin in Moodle takes the form of a folder containing files. The plugin has a type and a name, which together make up the "Frankenstyle" component name of the plugin[^4]. The plugin type and name determine the path to the plugin folder. The plugin type gives a prefix, and the foldername is the plugin name. Here are some examples:

  ----------------------- ----------------- --------------------- ------------------------------
  **Plugin type**         **Plugin name**   **Frankenstyle**      **Folder**
  mod (Activity module)   `forum`           `mod_forum`           `mod/forum`
  mod (Activity module)   `quiz`            `mod_quiz`            `mod/quiz`
  block (Side-block)      `navigation`      `block_navigation`    `blocks/navigation`
  qtype (Question type)   `shortanswer`     `qtype_shortanswer`   `question/type`/shortanswer
  quiz (Quiz report)      `statistics`      `quiz_statistics`     `mod/quiz/report/statistics`
  ----------------------- ----------------- --------------------- ------------------------------

The last example shows that each activity module is allowed to declare sub-plugin types. At the moment only activity modules can do this, for two reasons. If all plugins could have sub-plugins that might cause performance problems. Activity modules are the main educational activities in Moodle, and so are the most important type of plugin, thus they get special privileges.

### An Example Plugin

I will explain a lot of details of the Moodle architecture by considering a specific example plugin. As is traditional, I have chosen to implement a plugin that displays "Hello world".

This plugin does not really fit naturally into any of the standard Moodle plugin types. It is just a script, with no connection to anything else, so I will choose to implement it as a "local" plugin. This is a catch-all plugin type for miscellaneous functionality that does not fit anywhere better. I will name my plugin `greet`, to give a Frankensyle name of `local_greet`, and a folder path of `local/greet`.[^5]

Each plugin must contain a file called `version.php` which defines some basic metadata about the plugin. This is used by the Moodle's plugin installer system to install and upgrade the plugin. For example, `local/greet/version.php` contains:

    <?php
    $plugin->component    = 'local_greet';
    $plugin->version      = 2011102900;
    $plugin->requires     = 2011102700;
    $plugin->maturity     = MATURITY_STABLE;

It may seem redundant to include the component name, since this can be deduced from the path, but the installer uses this to verify that the plugin has been installed in the right place. The version field is the version of this plugin. Maturity is ALPHA, BETA, RC (release candidate), or STABLE. Requires is the minimum version of Moodle that this plugin is compatible with. If necessary, one can also document other plugins that this one depends on.

Here is the main script for this simple plugin (stored in `local/greet/index.php`):

    <?php
    require_once(dirname(__FILE__) . '/../../config.php');        // 1

    require_login();                                              // 2
    $context = context_system::instance();                        // 3
    require_capability('local/greet:begreeted', $context);        // 4

    $name = optional_param('name', '', PARAM_TEXT);               // 5
    if (!$name) {
        $name = fullname($USER);                                  // 6
    }

    add_to_log(SITEID, 'local_greet', 'begreeted',
            'local/greet/index.php?name=' . urlencode($name));    // 7

    $PAGE->set_context($context);                                 // 8
    $PAGE->set_url(new moodle_url('/local/greet/index.php'),
            array('name' => $name));                              // 9
    $PAGE->set_title(get_string('welcome', 'local_greet'));       // 10

    echo $OUTPUT->header();                                       // 11
    echo $OUTPUT->box(get_string('greet', 'local_greet',
            format_string($name)));                               // 12
    echo $OUTPUT->footer();                                       // 13

### Line 1: Bootstrapping Moodle

    require_once(dirname(__FILE__) . '/../../config.php');        // 1

The single line of this script that does the most work is the first. I said above that `config.php` contains the details Moodle needs to connect to the database and find the moodledata folder. It ends, however, with the line `require_once(’lib/setup.php’)`. This:

1.  loads all the standard Moodle libraries using `require_once`;

2.  starts the session handling;

3.  connects to the database; and

4.  sets up a number of global variables, which we shall meet later.

### Line 2: Checking the User Is Logged In

    require_login();                                              // 2

This line causes Moodle to check that the current user is logged in, using whatever authentication plugin the administrator has configured. If not, the user will be redirected to the log-in form, and this function will never return.

A script that was more integrated into Moodle would pass more arguments here, to say which course or activity this page is part of, and then `require_login` would also verify that the user is enrolled in, or otherwise allowed to access this course, and is allowed to see this activity. If not, an appropriate error would be displayed.

## Moodle's Roles and Permissions System

The next two lines of code show how to check that the user has permission to do something. As you can see, from the developer's point of view, the API is very simple. Behind the scenes, however, there is a sophisticated access system which gives the administrator great flexibility to control who can do what.

### Line 3: Getting the Context

    $context = context_system::instance();                        // 3

In Moodle, users can have different permissions in different places. For example, a user might be a Teacher in one course, and a Student in another, and so have different permissions in each place. These places are called *contexts*. Contexts in Moodle form a hierarchy rather like a folder hierarchy in a file-system. At the top level is the System context (and, since this script is not very well integrated into Moodle, it uses that context).

Within the System context are a number of contexts for the different categories that have been created to organise courses. These can be nested, with one category containing other categories. Category contexts can also contain Course contexts. Finally, each activity in a course will have its own Module context.

![Figure 3: Contexts](contexts.png)

### Line 4: Checking the User Has Permission to Use This Script

    require_capability('local/greet:begreeted', $context);        // 4

Having got the context---the relevant area of Moodle---the permission can be checked. Each bit of functionality that a user may or may not have is called a *capability*. Checking a capability provides more fine-grained access control than the basic checks performed by `require_login`. Our simple example plugin has just one capability: `local/greet:begreeted`.

The check is done using the `require_capability` function, which takes the capability name and the context. Like other `require_``…` functions, it will not return if the user does not have the capability. It will display an error instead. In other places the non-fatal `has_capability` function, which returns a Boolean would be used, for example, to determine whether to display a link to this script from another page.

How does the administrator configure which user has which permission? Here is the calculation that `has_capability` performs (at least conceptually):

1.  Start from the current Context.

2.  Get a list of the Roles that the user has in this Context.

3.  Then work out what the Permission is for each Role in this Context.

4.  Aggregate those permissions to get a final answer.

### Defining Capabilities

As the example shows, a plugin can define new capabilities relating to the particular functionality it provides. Inside each Moodle plugin there is a sub-folder of the code called `db`. This contains all the information required to install or upgrade the plugin. One of those bits of information is a file called `access.php` that defines the capabilities. Here is the `access.php` file for our plugin, which lives in `local/greet/db/access.php`:

    <?php
    $capabilities = array('local/greet:begreeted' => array(
        'captype' => 'read',
        'contextlevel' => CONTEXT_SYSTEM,
        'archetypes' => array('guest' => CAP_ALLOW, 'user' => CAP_ALLOW)
    ));

This gives some metadata about each capability which are used when constructing the permissions management user interface. It also give default permissions for common types of role.

### Roles

The next part of the Moodle permissions system is roles. A *role* is really just a named set of permissions. When you are logged into Moodle, you will have the "Authenticated user" role in the System context, and since the System context is the root of the hierarchy, that role will apply everywhere.

Within a particular course, you may be a Student, and that role assignment will apply in the Course context and all the Module contexts within it. In another course, however, you may have a different role. For example, Mr Gradgrind may be Teacher in the "Facts, Facts, Facts" course, but a Student in the professional development course "Facts Aren't Everything". Finally, a user might be given the Moderator role in one particular forum (Module context).

### Permissions

A role defines a *permission* for each capability. For example the Teacher role will probably ALLOW `moodle/course:manage`, but the Student role will not. However, both Student and Teacher will allow `mod/forum:startdiscussion`.

The roles are normally defined globally, but they can be re-defined in each context. For example, one particular wiki can be made read-only to students by overriding the permission for the `mod/wiki:edit` capability for the Student role in that wiki (Module) context, to PREVENT.

There are four Permissions:

- NOT SET/INHERIT (default)

- ALLOW

- PREVENT

- PROHIBIT

In a given context, a role will have one of these four permissions for each capability. One difference between PROHIBIT and PREVENT is that a PROHIBIT cannot be overridden in sub-contexts.

### Permission Aggregation

Finally the permissions for all the roles the user has in this context are aggregated.

- If any role gives the permission PROHIBIT for this capability, return false.

- Otherwise, if any role gives ALLOW for this capability, return true.

- Otherwise return false.

A use case for PROHIBIT is this: Suppose a user has been making abusive posts in a number of forums, and we want to stop them immediately. We can create a Naughty user role, which sets `mod/forum:post` and other such capabilities to PROHIBIT. We can then assign this role to the abusive user in the System context. That way, we can be sure that the user will not be able to post any more in any forum. (We would then talk to the student, and having reached a satisfactory outcome, remove that role assignment so that they may use the system again.)

So, Moodle's permissions system gives administrators a huge amount of flexibility. They can define whichever roles they like with different permissions for each capability; they can alter the role definitions in sub-contexts; and then they can assign different roles to users in different contexts.

## Back to Our Example Script

The next part of the script illustrates some miscellaneous points:

### Line 5: Get Data From the Request

    $name = optional_param('name', '', PARAM_TEXT);               // 5

Something that every web application has to do is get data from a request (GET or POST variables) without being susceptible to SQL injection or cross-site scripting attacks. Moodle provides two ways to do this.

The simple method is the one shown here. It gets a single variable given the parameter name (here `name`) a default value, and the expected type. The expected type is used to clean the input of all unexpected characters. There are numerous types like `PARAM_INT`, `PARAM_ALPHANUM`, `PARAM_EMAIL`, and so on.

There is also a similar `required_param` function, which like other `require_``…` functions stops execution and displays an error message if the expected parameter is not found.

The other mechanism Moodle has for getting data from the request is a fully fledged forms library. This is a wrapper around the HTML QuickForm library from PEAR[^6]. This seemed like a good choice when it was selected, but is now no longer maintained. At some time in the future we will have to tackle moving to a new forms library, which many of us look forwards to, because QuickForm has several irritating design issues. For now, however, it is adequate. Forms can be defined as a collection of fields of various types (e.g. text box, select drop-down, date-selector) with client- and server- side validation (including use of the same `PARAM_``…` types).

### Line 6: Global Variables

    if (!$name) {
        $name = fullname($USER);                                  // 6
    }

This snippet shows the first of the global variables Moodle provides. `$USER` makes accessible the information about the user accessing this script. Other globals include:

- `$CFG`: holds the commonly used configuration settings.

- `$DB`: the database connection.

- `$SESSION`: a wrapper around the PHP session.

- `$COURSE`: the course the current request relates to.

and several others, some of which we will encounter below.

You may have read the words "global variable" with horror. Note, however, that PHP processes a single request at a time. Therefore these variables are not as global as all that. In fact, PHP global variables can be seen as an implementation of the thread-scoped registry pattern[^7] and this is the way in which Moodle uses them. It is very convenient in that it makes commonly used objects available throughout the code, without requiring them to be passed to every function and method. It is only infrequently abused.

### Nothing is Simple

This line also serves to make a point about the problem domain: nothing is ever simple. To display a user's name is more complicated than simply concatenating `$USER->firstname`, `’ ’`, and `$USER->lastname`. The school may have policies about showing either of those parts, and different cultures have different conventions for which order to show names. Therefore, there are several configurations settings and a function to assemble the full name according to the rules.

Dates are a similar problem. Different users may be in different time-zones. Moodle stores all dates as Unix time-stamps, which are integers, and so work in all databases. There is then a `userdate` function to display the time-stamp to the user using the appropriate timezone and locale settings.

### Line 7: Logging

    add_to_log(SITEID, 'local_greet', 'begreeted',
            'local/greet/index.php?name=' . urlencode($name));    // 7

All significant actions in Moodle are logged. Logs are written to a table in the database. This is a trade-off. It makes sophisticated analysis quite easy, and indeed various reports based on the logs are included with Moodle. On a large and busy site, however, it is a performance problem. The log table gets huge, which makes backing up the database more difficult, and makes queries on the log table slow. There can also be write contention on the log table. These problems can be mitigated in various ways, for example by batching writes, or archiving or deleting old records to remove them from the main database.

## Generating Output

Output is mainly handled via two global objects.

### Line 8: The `$PAGE` Global

    $PAGE->set_context($context);                                 // 8

`$PAGE` stores the information about the page to be output. This information is then readily available to the code that generates the HTML. This script needs to explicitly specify the current context. (In other situations, this might have been set automatically by `require_login`.) The URL for this page must also be set explicitly. This may seem redundant, but the rationale for requiring it is that you might get to a particular page using any number of different URLs, but the URL passed to `set_url` should be the canonical URL for the page---a good permalink, if you like. The page title is also set. This will end up in the `head` element of the HTML.

### Line 9: Moodle URL

    $PAGE->set_url(new moodle_url('/local/greet/index.php'),
            array('name' => $name));                              // 9

I just wanted to flag this nice little helper class which makes manipulating URLs much easier. As an aside, recall that the `add_to_log` function call above did not use this helper class. Indeed, the log API cannot accept `moodle_url` objects. This sort of inconsistency is a typical sign of a code-base as old as Moodle's.

### Line 10: Internationalisation

    $PAGE->set_title(get_string('welcome', 'local_greet'));       // 10

Moodle uses its own system to allow the interface to be translated into any language. There may now be good PHP internationalisation libraries, but in 2002 when it was first implemented there was not one available that was adequate. The system is based around the `get_string` function. Strings are identified by a key and the plugin Frankenstyle name. As can be seen on line 12, it is possible to interpolate values into the string. (Multiple values are handled using PHP arrays or objects.)

The strings are looked up in language files that are just plain PHP arrays. Here is the language file `local/greet/lang/en/local_greet.php` for our plugin:

    <?php
    $string['greet:begreeted'] = 'Be greeted by the hello world example';
    $string['welcome'] = 'Welcome';
    $string['greet'] = 'Hello, {$a}!';
    $string['pluginname'] = 'Hello world example';

Note that, as well as the two string used in our script, there are also strings to give a name to the capability, and the name of the plugin as it appears in the user interface.

The different languages are identified by the two-letter country code (`en` here). Languages packs may derive from other language packs. For example the `fr_ca` (French Canadian) language pack declares `fr` (French) as the parent language, and thus only has to define those strings that differ from the French. Since Moodle originated in Australia, `en` means British English, and `en_us` (American English) is derived from it.

Again, the simple `get_string` API for plugin developers hides a lot of complexity, including working out the current language (which may depend on the current user's preferences, or the settings for the particular course they are currently in), and then searching through all the language packs and parent language packs to find the string.

Producing the language pack files, and co-ordinating the translation effort is managed at <http://lang.moodle.org/>, which is Moodle with a custom plugin[^8]. It uses both Git and the database as a backend to store the language files with full version history.

### Line 11: Starting Output

    echo $OUTPUT->header();                                       // 11

This is another innocuous-looking line that does much more than it seems. The point is that before any output can be done, the applicable theme (skin) must be worked out. This may depend on a combination of the page context and the user's preferences. `$PAGE-``>``context` was, however, only set on line 8, so the `$OUTPUT` global could not have been initialised at the start of the script. In order to solve this problem, some PHP magic is used to create the proper `$OUTPUT` object based on the information in `$PAGE` the first time any output method is called.

Another thing to consider is that every page in Moodle may contain *blocks*. These are extra configurable bits of content that are normally displayed to the left or right of the main content. (They are a type of plugin.) Again, the exact collection of blocks to display depends, in a flexible way (that the administrator can control) on the page context and some other aspects of the page identity. Therefore, another part of preparing for output is a call to `$PAGE-``>``blocks-``>``load_blocks()`.

Once all the necessary information has been worked out, the theme plugin (that controls the overall look of the page) is called to generate the overall page layout, including whatever standard header and footer is desired. This call is also responsible for adding the output from the blocks at the appropriate place in the HTML. In the middle of the layout there will be a `div` where the specific content for this page goes. The HTML of this layout is generated, and then split in half after the start of the main content `div`. The first half is returned, and the rest is stored to be returned by `$OUTPUT-``>``footer()`.

### Line 12: Outputting the Body of the Page

    echo $OUTPUT->box(get_string('greet', 'local_greet',
            format_string($name)));                               // 12

This line outputs the body of the page. Here it simply displays the greeting in a box. The greeting is, again, a localised string, this time with a value substituted into a placeholder. The core renderer `$OUTPUT` provides many convenience methods like `box` to describe the required output in quite high-level terms. Different themes can control what HTML is actually output to make the box.

The content that originally came from the user (`$name`) is output though the `format_string` function. This is the other part of providing XSS protection. It also enables the user of text filters (another plugin type). An example filter would be the LaTeX filter, which replaces input like `$$x + 1$$` with an image of the equation. I will mention, but not explain, that there are actually three different functions (`s`, `format_string`, and `format_text`) depending on the particular type of content being output.

### Line 13: Finishing Output

    echo $OUTPUT->footer();                                       // 13

Finally, the footer of the page is output. This example does not show it, but Moodle tracks all the JavaScript that is required by the page, and outputs all the necessary script tags in the footer. This is standard good practice. It allows users to see the page without waiting for all the JavaScript to load. A developer would include JavaScript using API calls like `$PAGE-``>``requires-``>``js(’/local/greet/cooleffect.js’)`.

### Should This Script Mix Logic and Output?

Obviously, putting the output code directly in `index.php`, even if at a high level of abstraction, limits the flexibility that themes have to control the output. This is another sign of the age of the Moodle code-base. The `$OUTPUT` global was introduced in 2010 as a stepping stone on the way from the old code, where the output and controller code were in the same file, to a design where all the view code was properly separated. This also explains the rather ugly way that the entire page layout is generated, then split in half, so that any output from the script itself can be placed between the header and the footer. Once the view code has been separated out of the script, into what Moodle calls a renderer, the theme can then choose to completely (or partially) override the view code for a given script.

A small refactoring can move all the output code out of our `index.php` and into a renderer. The end of `index.php` (lines 11 to 13) would change to:

    $output = $PAGE->get_renderer('local_greet');
    echo $output->greeting_page($name);

and there would be a new file `local/greet/renderer.php`:

    <?php
    class local_greet_renderer extends plugin_renderer_base {
        public function greeting_page($name) {
            $output = '';
            $output .= $this->header();
            $output .= $this->box(get_string('greet', 'local_greet', $name));
            $output .= $this->footer();
            return $output;
        }
    }

If the theme wished to completely change this output, it would define a subclass of this renderer that overrides the `greeting_page` method. `$PAGE-``>``get_renderer()` determines the appropriate renderer class to instantiate depending on the current theme. Thus, the output (view) code is fully separated from the controller code in `index.php`, and the plugin has been refactored from typical legacy Moodle code to a clean MVC architecture.

## Database Abstraction

The \"Hello world\" script was sufficiently simple that it did not need to access the database, although several of the Moodle library calls used did do database queries. I will now briefly describe the Moodle database layer.

Moodle used to use the ADOdb library as the basis of its database abstraction layer, but there were issues for us, and the extra layer of library code had a noticeable impact on performance. Therefore, in Moodle 2.0 we switched to our own abstraction layer, which is a thin wrapper around the various PHP database libraries.

### The `moodle_database` Class

The heart of the library is the `moodle_database` class. This defines the interface provided by the `$DB` global variable, which gives access to the database connection. A typical usage might be:

    $course = $DB->get_record('course', array('id' => $courseid));

That translates into the SQL:

    SELECT * FROM mdl_course WHERE id = $courseid;

and returns the data as a plain PHP object with public fields, so you could access `$course-``>``id`, `$course-``>``fullname`, etc.

Simple methods like this deal with basic queries, and simple updates and inserts. Sometimes it is necessary to do more complex SQL, for example to run reports. In that case, there are methods to execute arbitrary SQL:

    $courseswithactivitycounts = $DB->get_records_sql(
       'SELECT c.id, ' . $DB->sql_concat('shortname', "' '", 'fullname') . ' AS coursename,
            COUNT(1) AS activitycount
       FROM {course} c
       JOIN {course_modules} cm ON cm.course = c.id
       WHERE c.category = :categoryid
       GROUP BY c.id, c.shortname, c.fullname ORDER BY c.shortname, c.fullname',
       array('categoryid' => $category));

Some things to note there:

- The table names are wrapped in `{}` so that the library can find them and prepend the table name prefix.

- The library uses placeholders to insert values into the SQL. In some cases this uses the facilities of the underlying database driver. In other cases the values have to be escaped and inserted into the SQL using string manipulation. The library supports both named placeholders (as above) and anonymous ones, using `?` as the placeholder.

- For queries to work on all our supported databases a safe subset of standard SQL must be used. For example, you can see that I have used the `AS` keyword for column aliases, but not for table aliases. Both of these usage rules are necessary.

- Even so, there are some situations where no subset of standard SQL will work on all our supported databases; for example, every database has a different way to concatenate strings. In these cases there are compatibility functions to generate the correct SQL.

### Defining the Database Structure

Another area where database management systems differ a lot is in the SQL syntax required to define tables. To get around this problem, each Moodle plugin (and Moodle core) defines the required database tables in an XML file. The Moodle install system parses the `install.xml` files and uses the information they contain to create the required tables and indexes. There is a developer tool called XMLDB built into Moodle to help create and edit these install files.

If the database structure needs to change between two releases of Moodle (or of a plugin) then the developer is responsible for writing code (using an additional database object that provides DDL methods) to update the database structure, while preserving all the users' data. Thus, Moodle will always self-update from one release to the next, simplifying maintenance for administrators.

One contentious point, stemming from the fact that Moodle started out using MySQL 3, is that the Moodle database does not use foreign keys. This allows some buggy behaviour to remain undetected even though modern databases would be capable of detecting the problem. The difficulty is that people have been running Moodle sites without foreign keys for years, so there is almost certainly inconsistent data present. Adding the keys now would be impossible, without a very difficult clean-up job. Even so, since the XMLDB system was added to Moodle 1.7 (in 2006!) the install.xml files have contained the definitions of the foreign keys that should exist, and we are still hoping, one day, to do all the work necessary to allow us to create them during the install process.

## What Has Not Been Covered

I hope I have given you a good overview of how Moodle works. Due to lack of space I have had to omit several interesting topics, including how authentication, enrolment and grade plugins allow Moodle to interoperate with student information systems, and the interesting content-addressed way that Moodle stores uploaded files. Details of these, and other aspects of Moodle's design, can be found in the developer documentation[^9].

## Lessons Learned

One interesting aspect of working on Moodle is that it came out of a research project. Moodle enables (but does not enforce) a social constructivist pedagogy[^10]. That is, we learn best by actually creating something, and we learn from each other as a community. Martin Dougiamas's PhD question did not ask whether this was an effective model for education, but rather whether it is an effective model for running an open source project. That is, can we view the Moodle project as an attempt to learn how to build and use a VLE, and an attempt to learn that by actually building and using Moodle as a community where teachers, developers, administrators and students all teach and learn from each other? I find this a good model for thinking about an open source software development project. The main place where developers and users learn from each other is in discussions in the Moodle project forums, and in the bug database.

Perhaps the most important consequence of this learning approach is that you should not be afraid to start by implementing the simplest possible solution first. For example, early versions of Moodle had just a few hard-coded roles like Teacher, Student and Administrator. That was enough for many years, but eventually the limitations had to be addressed. When the time came to design the Roles system for Moodle 1.7, there was a lot of experience in the community about how people were using Moodle, and many little feature requests that showed what people needed to be able to adjust using a more flexible access control system. This all helped design the Roles system to be as simple as possible, but as complex as necessary. (In fact, the first version of the roles system ended up slightly too complex, and it was subsequently simplified a little in Moodle 2.0.)

If you take the view that programming is a problem-solving exercise, then you might think that Moodle got the design wrong the first time, and later had to waste time correcting it. I suggest that is an unhelpful viewpoint when trying to solve complex real-world problems. At the time Moodle started, no-one knew enough to design the roles system we now have. If you take the learning viewpoint, then the various stages Moodle went through to reach the current design were necessary and inevitable.

For this perspective to work, it must be possible to change almost any aspect of a system's architecture once you have learned more. I think Moodle shows that this is possible. For example, we found a way for code to be gradually refactored from legacy scripts to a cleaner MVC architecture. This requires effort, but it seems that when necessary, the resources to implement these changes can be found in open source projects. From the user's point of view, the system gradually evolves with each major release.

[^1]: <http://moodle.org/>

[^2]: This is a good property for URLs to have, as explained in Tim Berners-Lee's article *Cool URIs don't change* <http://www.w3.org/Provider/Style/URI.html>

[^3]: For a full list of Moodle plugin types see <http://docs.moodle.org/dev/Plugins>.

[^4]: The word "Frankenstyle" arose out of an argument in the developers' Jabber channel, but everyone liked it and it stuck.

[^5]: The plugin code can be downloaded from <https://github.com/timhunt/moodle-local_greet>.

[^6]: For non-PHP programmers, PEAR is PHP's equivalent of CPAN.

[^7]: See Martin Fowler's *Patterns of Enterprise Application Architecture*.

[^8]: `local_amos`, <http://docs.moodle.org/22/en/AMOS>.

[^9]: <http://docs.moodle.org/dev/>

[^10]: <http://docs.moodle.org/22/en/Pedagogy>
