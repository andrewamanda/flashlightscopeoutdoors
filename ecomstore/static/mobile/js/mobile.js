(function(d, c) {
    d.widget("mobile.simpledialog2", d.mobile.widget, {
        options: {
            version: "1.0.1-2012022700",
            mode: "blank",
            themeDialog: "b",
            themeInput: false,
            themeButtonDefault: false,
            themeHeader: "a",
            fullScreen: false,
            fullScreenForce: false,
            dialogAllow: false,
            dialogForce: false,
            headerText: false,
            headerClose: false,
            buttonPrompt: false,
            buttonInput: false,
            buttonPassword: false,
            blankContent: false,
            resizeListener: true,
            safeNuke: true,
            forceInput: true,
            showModal: true,
            animate: true,
            transition: "pop",
            clickEvent: "click",
            zindex: "500",
            width: "280px",
            left: false,
            top: false,
            callbackOpen: false,
            callbackOpenArgs: [],
            callbackClose: false,
            callbackCloseArgs: []
        },
        _eventHandler: function(b, e) {
            var h = b.data.widget,
                a = b.data.widget.options;
            if (!b.isPropagationStopped()) {
                switch (e.method) {
                    case "close":
                        h.close();
                        break;
                    case "html":
                        h.updateBlank(e.source);
                        break
                }
            }
        },
        _create: function() {
            var h = this,
                a = d.extend(this.options, this.element.jqmData("options")),
                b = new Date(),
                g = d("<div class='ui-simpledialog-container ui-overlay-shadow ui-corner-all ui-simpledialog-hidden " + ((a.animate === true) ? a.transition : "") + " ui-body-" + a.themeDialog + "'></div>");
            if (a.themeButtonDefault === false) {
                a.themeButtonDefault = a.themeDialog
            }
            if (a.themeInput === false) {
                a.themeInput = a.themeDialog
            }
            d.mobile.sdCurrentDialog = h;
            if (typeof d.mobile.sdLastInput !== "undefined") {
                delete d.mobile.sdLastInput
            }
            h.internalID = b.getTime();
            h.displayAnchor = d.mobile.activePage.children(".ui-content").first();
            h.dialogPage = d("<div data-role='dialog' class='ui-simpledialog-dialog' data-theme='" + a.themeDialog + "'><div data-role='header'></div><div data-role='content'></div></div>");
            h.sdAllContent = h.dialogPage.find("[data-role=content]");
            g.appendTo(h.sdAllContent);
            h.sdIntContent = h.sdAllContent.find(".ui-simpledialog-container");
            h.sdIntContent.css("width", a.width);
            if (a.headerText !== false || a.headerClose !== false) {
                h.sdHeader = d('<div style="margin-bottom: 4px;" class="ui-header ui-bar-' + a.themeHeader + '"></div>');
                if (a.headerClose === true) {
                    d("<a class='ui-btn-left' rel='close' href='#'>Close</a>").appendTo(h.sdHeader).buttonMarkup({
                        theme: a.themeHeader,
                        icon: "delete",
                        iconpos: "notext",
                        corners: true,
                        shadow: true
                    })
                }
                d('<h1 class="ui-title">' + ((a.headerText !== false) ? a.headerText : "") + "</h1>").appendTo(h.sdHeader);
                h.sdHeader.appendTo(h.sdIntContent)
            }
            if (a.mode === "blank") {
                if (a.blankContent === true) {
                    a.blankContent = h.element.html()
                }
                d(a.blankContent).appendTo(h.sdIntContent)
            } else {
                if (a.mode === "button") {
                    h._makeButtons().appendTo(h.sdIntContent)
                }
            }
            h.sdIntContent.appendTo(h.displayAnchor.parent());
            h.dialogPage.appendTo(d.mobile.pageContainer).page().css("minHeight", "0px").css("zIndex", a.zindex);
            if (a.animate === true) {
                h.dialogPage.addClass(a.transition)
            }
            h.screen = d("<div>", {
                "class": "ui-simpledialog-screen ui-simpledialog-hidden"
            }).css("z-index", (a.zindex - 1)).appendTo(h.displayAnchor.parent()).bind(a.clickEvent, function(e) {
                if (!a.forceInput) {
                    h.close()
                }
                e.preventDefault()
            });
            if (a.showModal) {
                h.screen.addClass("ui-simpledialog-screen-modal")
            }
            d(document).bind("simpledialog." + h.internalID, {
                widget: h
            }, function(e, f) {
                h._eventHandler(e, f)
            })
        },
        _makeButtons: function() {
            var i = this,
                a = i.options,
                b = d("<div></div>"),
                h = d("<div class='ui-simpledialog-controls'><input class='ui-simpledialog-input ui-input-text ui-shadow-inset ui-corner-all ui-body-" + a.themeInput + "' type='" + ((a.buttonPassword === true) ? "password" : "text") + "' name='pickin' /></div>"),
                j = d("<div>", {
                    "class": "ui-simpledialog-controls"
                });
            if (a.buttonPrompt !== false) {
                i.buttonPromptText = d("<p class='ui-simpledialog-subtitle'>" + a.buttonPrompt + "</p>").appendTo(b)
            }
            if (a.buttonInput !== false) {
                d.mobile.sdLastInput = "";
                h.appendTo(b);
                h.find("input").bind("change", function() {
                    d.mobile.sdLastInput = h.find("input").first().val();
                    i.thisInput = h.find("input").first().val()
                })
            }
            j.appendTo(b);
            i.butObj = [];
            d.each(a.buttons, function(f, e) {
                e = d.isFunction(e) ? {
                    click: e
                } : e;
                e = d.extend({
                    text: f,
                    id: f + i.internalID,
                    theme: a.themeButtonDefault,
                    icon: "check",
                    iconpos: "left",
                    corners: "true",
                    shadow: "true",
                    args: [],
                    close: true
                }, e);
                i.butObj.push(d("<a href='#'>" + f + "</a>").appendTo(j).attr("id", e.id).buttonMarkup({
                    theme: e.theme,
                    icon: e.icon,
                    iconpos: e.iconpos,
                    corners: e.corners,
                    shadow: e.shadow
                }).unbind("vclick click").bind(a.clickEvent, function() {
                    if (a.buttonInput) {
                        i.sdIntContent.find("input [name=pickin]").trigger("change")
                    }
                    var g = e.click.apply(i, d.merge(arguments, e.args));
                    if (g !== false && e.close === true) {
                        i.close()
                    }
                }))
            });
            return b
        },
        _getCoords: function(b) {
            var o = b,
                l = d.mobile.activePage.width(),
                n = d(window).scrollTop(),
                m = d(window).height(),
                p = b.sdIntContent.innerWidth(),
                a = b.sdIntContent.outerHeight(),
                k = {
                    high: d(window).height(),
                    width: d.mobile.activePage.width(),
                    fullTop: d(window).scrollTop(),
                    fullLeft: d(window).scrollLeft(),
                    winTop: n + ((b.options.top !== false) ? b.options.top : ((m / 2) - (a / 2))),
                    winLeft: ((b.options.left !== false) ? b.options.left : ((l / 2) - (p / 2)))
                };
            if (k.winTop < 45) {
                k.winTop = 45
            }
            return k
        },
        _orientChange: function(b) {
            var h = b.data.widget,
                a = b.data.widget.options,
                e = b.data.widget._getCoords(b.data.widget);
            b.stopPropagation();
            if (h.isDialog === true) {
                return true
            } else {
                if (a.fullScreen === true && (e.width < 400 || a.fullScreenForce === true)) {
                    h.sdIntContent.css({
                        border: "none",
                        position: "absolute",
                        top: e.fullTop,
                        left: e.fullLeft,
                        height: e.high,
                        width: e.width,
                        maxWidth: e.width
                    }).removeClass("ui-simpledialog-hidden")
                } else {
                    h.sdIntContent.css({
                        position: "absolute",
                        top: e.winTop,
                        left: e.winLeft
                    }).removeClass("ui-simpledialog-hidden")
                }
            }
        },
        repos: function() {
            var a = {
                data: {
                    widget: this
                },
                stopPropagation: function() {
                    return true
                }
            };
            this._orientChange(a)
        },
        open: function() {
            var f = this,
                a = this.options,
                b = this._getCoords(this);
            f.sdAllContent.find(".ui-btn-active").removeClass("ui-btn-active");
            f.sdIntContent.delegate("[rel=close]", a.clickEvent, function(e) {
                e.preventDefault();
                f.close()
            });
            if ((a.dialogAllow === true && b.width < 400) || a.dialogForce) {
                f.isDialog = true;
                if (a.mode === "blank") {
                    f.sdIntContent.find("select").each(function() {
                        d(this).jqmData("nativeMenu", true)
                    })
                }
                f.displayAnchor.parent().unbind("pagehide.remove");
                f.sdAllContent.append(f.sdIntContent);
                f.sdAllContent.trigger("create");
                if (a.headerText !== false) {
                    f.sdHeader.find("h1").appendTo(f.dialogPage.find("[data-role=header]"));
                    f.sdIntContent.find(".ui-header").empty().removeClass()
                }
                if (a.headerClose === true) {
                    f.dialogPage.find(".ui-header a").bind("click", function() {
                        setTimeout("$.mobile.sdCurrentDialog.destroy();", 1000)
                    })
                } else {
                    f.dialogPage.find(".ui-header a").remove()
                }
                f.sdIntContent.removeClass().css({
                    top: "auto",
                    width: "auto",
                    left: "auto",
                    marginLeft: "auto",
                    marginRight: "auto",
                    zIndex: a.zindex
                });
                d.mobile.changePage(f.dialogPage, {
                    transition: (a.animate === true) ? a.transition : "none"
                })
            } else {
                f.isDialog = false;
                f.selects = [];
                if (a.fullScreen === false) {
                    if (a.showModal === true && a.animate === true) {
                        f.screen.fadeIn("slow")
                    } else {
                        f.screen.removeClass("ui-simpledialog-hidden")
                    }
                }
                f.sdIntContent.addClass("ui-overlay-shadow in").css("zIndex", a.zindex).trigger("create");
                if (a.fullScreen === true && (b.width < 400 || a.fullScreenForce === true)) {
                    f.sdIntContent.removeClass("ui-simpledialog-container").css({
                        border: "none",
                        position: "absolute",
                        top: b.fullTop,
                        left: b.fullLeft,
                        height: b.high,
                        width: b.width,
                        maxWidth: b.width
                    }).removeClass("ui-simpledialog-hidden")
                } else {
                    f.sdIntContent.css({
                        position: "absolute",
                        top: b.winTop,
                        left: b.winLeft
                    }).removeClass("ui-simpledialog-hidden")
                }
                d(document).bind("orientationchange.simpledialog", {
                    widget: f
                }, function(e) {
                    f._orientChange(e)
                });
                if (a.resizeListener === true) {
                    d(window).bind("resize.simpledialog", {
                        widget: f
                    }, function(e) {
                        f._orientChange(e)
                    })
                }
            }
            if (d.isFunction(a.callbackOpen)) {
                a.callbackOpen.apply(f, a.callbackOpenArgs)
            }
        },
        close: function() {
            var b = this,
                a;
            if (d.isFunction(b.options.callbackClose)) {
                a = b.options.callbackClose.apply(b, b.options.callbackCloseArgs);
                if (a === false) {
                    return false
                }
            }
            if (b.isDialog) {
                d(b.dialogPage).dialog("close");
                b.sdIntContent.addClass("ui-simpledialog-hidden");
                b.sdIntContent.appendTo(b.displayAnchor.parent());
                if (d.mobile.activePage.jqmData("page").options.domCache != true) {
                    d.mobile.activePage.bind("pagehide.remove", function() {
                        d(this).remove()
                    })
                }
            } else {
                if (b.options.showModal === true && b.options.animate === true) {
                    b.screen.fadeOut("slow")
                } else {
                    b.screen.addClass("ui-simpledialog-hidden")
                }
                b.sdIntContent.addClass("ui-simpledialog-hidden").removeClass("in");
                d(document).unbind("orientationchange.simpledialog");
                if (b.options.resizeListener === true) {
                    d(window).unbind("resize.simpledialog")
                }
            }
            d.mobile.activePage.find(".ui-btn-active").removeClass("ui-btn-active");
            if (b.isDialog === true || b.options.animate === true) {
                setTimeout("$.mobile.sdCurrentDialog.destroy();", 1000)
            } else {
                b.destroy()
            }
        },
        destroy: function() {
            var b = this,
                a = b.element;
            if (b.options.mode === "blank") {
                d.mobile.sdCurrentDialog.sdIntContent.find("select").each(function() {
                    if (d(this).data("nativeMenu") == false) {
                        d(this).data("selectmenu").menuPage.remove();
                        d(this).data("selectmenu").screen.remove();
                        d(this).data("selectmenu").listbox.remove()
                    }
                })
            }
            d(b.sdIntContent).remove();
            d(b.dialogPage).remove();
            d(b.screen).remove();
            d(document).unbind("simpledialog." + b.internalID);
            delete d.mobile.sdCurrentDialog;
            d.Widget.prototype.destroy.call(b);
            if (b.options.safeNuke === true && d(a).parents().length === 0 && d(a).contents().length === 0) {
                a.remove()
            }
        },
        updateBlank: function(a) {
            var f = this,
                b = this.options;
            f.sdIntContent.empty();
            if (b.headerText !== false || b.headerClose !== false) {
                f.sdHeader = d('<div class="ui-header ui-bar-' + b.themeHeader + '"></div>');
                if (b.headerClose === true) {
                    d("<a class='ui-btn-left' rel='close' href='#'>Close</a>").appendTo(f.sdHeader).buttonMarkup({
                        theme: b.themeHeader,
                        icon: "delete",
                        iconpos: "notext",
                        corners: true,
                        shadow: true
                    })
                }
                d('<h1 class="ui-title">' + ((b.headerText !== false) ? b.headerText : "") + "</h1>").appendTo(f.sdHeader);
                f.sdHeader.appendTo(f.sdIntContent)
            }
            d(a).appendTo(f.sdIntContent);
            f.sdIntContent.trigger("create");
            d(document).trigger("orientationchange.simpledialog")
        },
        _init: function() {
            this.open()
        }
    })
})(jQuery);
var store = function() {
    var q = {},
        k = window,
        h = k.document,
        l;
    q.disabled = false;
    q.set = function() {};
    q.get = function() {};
    q.remove = function() {};
    q.clear = function() {};
    q.transact = function(b, g) {
        var f = q.get(b);
        if (typeof f == "undefined") {
            f = {}
        }
        g(f);
        q.set(b, f)
    };
    q.serialize = function(b) {
        return JSON.stringify(b)
    };
    q.deserialize = function(b) {
        if (typeof b == "string") {
            return JSON.parse(b)
        }
    };
    var c;
    try {
        c = "localStorage" in k && k.localStorage
    } catch (j) {
        c = false
    }
    if (c) {
        l = k.localStorage;
        q.set = function(b, f) {
            l.setItem(b, q.serialize(f))
        };
        q.get = function(b) {
            return q.deserialize(l.getItem(b))
        };
        q.remove = function(b) {
            l.removeItem(b)
        };
        q.clear = function() {
            l.clear()
        }
    } else {
        var e;
        try {
            e = "globalStorage" in k && k.globalStorage && k.globalStorage[k.location.hostname]
        } catch (a) {
            e = false
        }
        if (e) {
            l = k.globalStorage[k.location.hostname];
            q.set = function(b, f) {
                l[b] = q.serialize(f)
            };
            q.get = function(b) {
                return q.deserialize(l[b] && l[b].value)
            };
            q.remove = function(b) {
                delete l[b]
            };
            q.clear = function() {
                for (var b in l) {
                    delete l[b]
                }
            }
        } else {
            if (h.documentElement.addBehavior) {
                l = h.createElement("div");
                k = function(b) {
                    return function() {
                        var f = Array.prototype.slice.call(arguments, 0);
                        f.unshift(l);
                        h.body.appendChild(l);
                        l.addBehavior("#default#userData");
                        l.load("localStorage");
                        f = b.apply(q, f);
                        h.body.removeChild(l);
                        return f
                    }
                };
                q.set = k(function(b, g, f) {
                    b.setAttribute(g, q.serialize(f));
                    b.save("localStorage")
                });
                q.get = k(function(b, f) {
                    return q.deserialize(b.getAttribute(f))
                });
                q.remove = k(function(b, f) {
                    b.removeAttribute(f);
                    b.save("localStorage")
                });
                q.clear = k(function(b) {
                    var i = b.XMLDocument.documentElement.attributes;
                    b.load("localStorage");
                    for (var g = 0, f; f = i[g]; g++) {
                        b.removeAttribute(f.name)
                    }
                    b.save("localStorage")
                })
            }
        }
    }
    try {
        q.set("__storejs__", "__storejs__");
        if (q.get("__storejs__") != "__storejs__") {
            q.disabled = true
        }
        q.remove("__storejs__")
    } catch (d) {
        q.disabled = true
    }
    return q
}();
if (!this.JSON) {
    this.JSON = {}
}(function() {
    function b(a) {
        return a < 10 ? "0" + a : a
    }

    function g(a) {
        p.lastIndex = 0;
        return p.test(a) ? '"' + a.replace(p, function(c) {
            var d = r[c];
            return typeof d === "string" ? d : "\\u" + ("0000" + c.charCodeAt(0).toString(16)).slice(-4)
        }) + '"' : '"' + a + '"'
    }

    function m(a, c) {
        var d, h, k, q, l = i,
            j, e = c[a];
        if (e && typeof e === "object" && typeof e.toJSON === "function") {
            e = e.toJSON(a)
        }
        if (typeof o === "function") {
            e = o.call(c, a, e)
        }
        switch (typeof e) {
            case "string":
                return g(e);
            case "number":
                return isFinite(e) ? String(e) : "null";
            case "boolean":
            case "null":
                return String(e);
            case "object":
                if (!e) {
                    return "null"
                }
                i += n;
                j = [];
                if (Object.prototype.toString.apply(e) === "[object Array]") {
                    q = e.length;
                    for (d = 0; d < q; d += 1) {
                        j[d] = m(d, e) || "null"
                    }
                    k = j.length === 0 ? "[]" : i ? "[\n" + i + j.join(",\n" + i) + "\n" + l + "]" : "[" + j.join(",") + "]";
                    i = l;
                    return k
                }
                if (o && typeof o === "object") {
                    q = o.length;
                    for (d = 0; d < q; d += 1) {
                        h = o[d];
                        if (typeof h === "string") {
                            if (k = m(h, e)) {
                                j.push(g(h) + (i ? ": " : ":") + k)
                            }
                        }
                    }
                } else {
                    for (h in e) {
                        if (Object.hasOwnProperty.call(e, h)) {
                            if (k = m(h, e)) {
                                j.push(g(h) + (i ? ": " : ":") + k)
                            }
                        }
                    }
                }
                k = j.length === 0 ? "{}" : i ? "{\n" + i + j.join(",\n" + i) + "\n" + l + "}" : "{" + j.join(",") + "}";
                i = l;
                return k
        }
    }
    if (typeof Date.prototype.toJSON !== "function") {
        Date.prototype.toJSON = function() {
            return isFinite(this.valueOf()) ? this.getUTCFullYear() + "-" + b(this.getUTCMonth() + 1) + "-" + b(this.getUTCDate()) + "T" + b(this.getUTCHours()) + ":" + b(this.getUTCMinutes()) + ":" + b(this.getUTCSeconds()) + "Z" : null
        };
        String.prototype.toJSON = Number.prototype.toJSON = Boolean.prototype.toJSON = function() {
            return this.valueOf()
        }
    }
    var f = /[\u0000\u00ad\u0600-\u0604\u070f\u17b4\u17b5\u200c-\u200f\u2028-\u202f\u2060-\u206f\ufeff\ufff0-\uffff]/g,
        p = /[\\\"\x00-\x1f\x7f-\x9f\u00ad\u0600-\u0604\u070f\u17b4\u17b5\u200c-\u200f\u2028-\u202f\u2060-\u206f\ufeff\ufff0-\uffff]/g,
        i, n, r = {
            "\u0008": "\\b",
            "\t": "\\t",
            "\n": "\\n",
            "\u000c": "\\f",
            "\r": "\\r",
            '"': '\\"',
            "\\": "\\\\"
        },
        o;
    if (typeof JSON.stringify !== "function") {
        JSON.stringify = function(a, c, d) {
            var h;
            n = i = "";
            if (typeof d === "number") {
                for (h = 0; h < d; h += 1) {
                    n += " "
                }
            } else {
                if (typeof d === "string") {
                    n = d
                }
            }
            if ((o = c) && typeof c !== "function" && (typeof c !== "object" || typeof c.length !== "number")) {
                throw Error("JSON.stringify")
            }
            return m("", {
                "": a
            })
        }
    }
    if (typeof JSON.parse !== "function") {
        JSON.parse = function(a, c) {
            function d(k, q) {
                var l, j, e = k[q];
                if (e && typeof e === "object") {
                    for (l in e) {
                        if (Object.hasOwnProperty.call(e, l)) {
                            j = d(e, l);
                            if (j !== undefined) {
                                e[l] = j
                            } else {
                                delete e[l]
                            }
                        }
                    }
                }
                return c.call(k, q, e)
            }
            var h;
            a = String(a);
            f.lastIndex = 0;
            if (f.test(a)) {
                a = a.replace(f, function(k) {
                    return "\\u" + ("0000" + k.charCodeAt(0).toString(16)).slice(-4)
                })
            }
            if (/^[\],:{}\s]*$/.test(a.replace(/\\(?:["\\\/bfnrt]|u[0-9a-fA-F]{4})/g, "@").replace(/"[^"\\\n\r]*"|true|false|null|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?/g, "]").replace(/(?:^|:|,)(?:\s*\[)+/g, ""))) {
                h = eval("(" + a + ")");
                return typeof c === "function" ? d({
                    "": h
                }, "") : h
            }
            throw new SyntaxError("JSON.parse")
        }
    }
})();

function autoExpandContainer(b, f) {
    var c;
    if (!f.toPage) {
        return
    }
    if (typeof f.toPage === "string") {
        c = f.toPage
    } else {
        c = f.toPage[0].baseURI
    }
    var i = $.mobile.path.parseUrl(c);
    if (i.hash.length > 1) {
        return
    }
    var a = i.search;
    if (a.length < 4) {
        return
    }
    a = a.substring(1);
    var j = new RegExp("^l=([^&]+)$");
    var e = j.exec(a);
    if (e != null) {
        var g = e[1];
        if (g) {
            var d = "." + g;
            $(d).trigger("expand");
            if (typeof f.toPage === "string" && b.type == "pagebeforechange" && $(d).length > 0) {
                var h = $.mobile.path.parseUrl($.mobile.activePage[0].baseURI);
                if (i.hrefNoSearch == h.hrefNoSearch) {
                    b.preventDefault();
                    $.mobile.silentScroll($(d).offset().top)
                }
            }
        }
    }
}

function populateNavigation(a) {
    var b = document.getElementById("navigationList");
    a.innerHTML = b.innerHTML
}

function hideCategoryDetails() {
    $(".categoryPage .product-long-desc").hide();
    $(".categoryPage .product-short-desc").show();
    $(".categoryPage .product-attributes").hide()
}

function showCategoryDetails() {
    $(".categoryPage .product-long-desc").show();
    $(".categoryPage .product-short-desc").hide();
    $(".categoryPage .product-attributes").show()
}

function add2CartPopup(d,e,i) {
    	    var k = $("<div/>").text(e);
            if (!i) {
                var l = $("<a/>").attr("href", "/checkout/checkout_begin/").data("role", "button").data("ajax", "false").text("Check out").button();
                k.append(l);
                var j = $("<a/>").attr("href", "/cart").data("role", "button").text("View Cart").button();
                k.append(j);
                if (window._gaq && d.itemsAdded) {
                    for (var c in d.itemsAdded) {
                        if (d.itemsAdded.hasOwnProperty(c)) {
                            var g = c;
                            var f = d.itemsAdded[c];
                            _gaq.push(["_trackEvent", "product", "addToCart", g, f]);
                            _gaq.push(["_trackEvent", "mobile", "addToCart"])
                        }
                    }
                }
            }
            var h = $("<a/>").attr("href", "#").data("role", "button").data("rel", "back").text("Close").button();
            k.append(h);
            $(document).simpledialog2({
                mode: "button",
                headerClose: false,
                buttonPrompt: e,
                buttons: {
                    "Check out": {
                        click: function() {
                            window.location = "/checkout/checkout_begin/";
                            return true
                        }
                    },
                    "Show Cart": {
                        click: function() {
                            $.mobile.changePage("/cart", {
                                reloadPage: true
                            });
                            return true
                        },
                        theme: "c"
                    },
                    Close: {
                        click: function() {
                            return true
                        },
                        icon: "delete",
                        theme: "c"
                    }
                }
            })
};

$(document).bind("pagechange", function(a, b) {
    autoExpandContainer(a, b);
    $(".navigationCollapsible").trigger("collapse")
    hideCategoryDetails();

    $(".swipe-notice").stop(true).show().css("opacity", 1).delay(3000).fadeOut(1000)
});
$(document).bind("pagebeforechange", function(a, b) {


    autoExpandContainer(a, b)
});
$(document).ready(function() {
    $(document).on("click", "li.footerHelpBtn a", function(b, a) {
        b.preventDefault();
        $("li.footerHelpBtn span.ui-icon").toggleClass("ui-icon-arrow-r ui-icon-arrow-d");
        $("li.footerHelpBtnSub").toggleClass("shown hidden");
        return false
    });
    $(document).on("click", ".navigationTitle", function(a, b) {
        if ($(this).parent().hasClass("ui-collapsible-collapsed")) {
            store.set("navigationExpanded", "collapse")
        } else {
            store.set("navigationExpanded", "expand")
        }
    });
    $(document).on("click", ".categoryPage .show-styles-button", function(a, b) {
        $(".categoryPage div.hidden-line").toggle();
        if ("none" == $(".categoryPage div.hidden-line").prop("style").display) {
            $(".categoryPage .show-styles-button").buttonMarkup({
                icon: "plus"
            })
        } else {
            $(".categoryPage .show-styles-button").buttonMarkup({
                icon: "minus"
            })
        }
    });
    $(document).on("swipeleft", ".main-category-image-swipable", function(a, b) {
        if (a.currentTarget) {
            var c = $(a.currentTarget).data("arraysuffix");
            rotateMainCategoryImageLeft(c)
        }
    });
    $(document).on("swiperight", ".main-category-image-swipable", function(a, b) {
        if (a.currentTarget) {
            var c = $(a.currentTarget).data("arraysuffix");
            rotateMainCategoryImageRight(c)
        }
    });
    $(document).on("click", ".slider-indicator .dot", function(b, c) {
        if (b.currentTarget) {
            var d = $(b.currentTarget).data("arraysuffix");
            var a = $(b.currentTarget).data("index");
            rotateMainCategoryImageTo(a, d)
        }
    });
    $(document).on("pageinit", ".categoryPage", function(a) {
        if (window.screen) {
            imageWidth = $(".categoryPage img.main-category-image").prop("width");
            availableWidth = (screen.availWidth - 30);
            if (imageWidth && imageWidth > 0 && imageWidth > availableWidth) {
                $(".categoryPage img.main-category-image").prop("width", availableWidth)
            }
        }
    });
    $(document).on("submit", ".addToCartFormWithPopup", function(b) {
        var a = $(this);
        b.preventDefault();
        $.ajaxSetup({
                type: 'POST',
            	dataType: "json",
                timeout: 30000,
                beforeSend: function(xhr, settings) {
                        if (!this.crossDomain) {
                                xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
                        }
                },
                error: function(xhr) {
                        // alert('Failed to add to shopping cart: ' + xhr.status + ' ' + xhr.statusText);
               }
        })
        $.post(a.attr("action"), a.serialize(), function(d) {
            var e;
            var i = true;
            if (!d) {
                e = "Unexpected error, please try again later."
            } else {
                if (d.errors) {
                    e = errors.join("<br/>")
                } else {
                    showShoppingBagSize(d.cartSize);
                    e = "This item was added to your shopping cart.";
                    i = false
                }
            }
	    add2CartPopup(d,e,i);
        })
    });
    $(document).on("submit", ".BuyItNowForm", function(b) {
        var pList = [];
        listItems = $("#list").find("li").each(function(){
                pQty = $(this).find('#quantity').val();
                var product = {
                        id: $(this).find("#product_id").val(),
                        qty: pQty,
                };

                if(pQty > 0) {
                        pList.push(product);
                }
        });
        var p = {
                products_chosen: pList,
        }
        b.preventDefault();
        $.ajaxSetup({
                type: 'POST',
            	dataType: "json",
                timeout: 30000,
                beforeSend: function(xhr, settings) {
                        if (!this.crossDomain) {
                                xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
                        }
                },
                error: function(xhr) {
                        //alert('Failed to add to shopping cart: ' + xhr.status + ' ' + xhr.statusText);
               }
        })
        $.post("/nameyourprice/buyitnow/", p, function(d) {
            var e;
            var i = true;
            if (!d) {
                e = "Unexpected error, please try again later."
            } else {
                if (d.errors) {
                    e = errors.join("<br/>")
                } else {
                    showShoppingBagSize(d.cartSize);
                    e = "This item was added to your cart.";
                    i = false
                }
            }
	    add2CartPopup(d,e,i);
	})
    });
    $(document).on("submit", ".MakeOfferForm", function(b) {
        b.preventDefault();
        if($(".BuyerOfferPrice").val() > 0) {
                offerprice = $(".BuyerOfferPrice").val()
        }
        else {
                offerprice = 0;
        }
  	buyer_comment = $("#buyer_comment").val();
  	shipping_country = $("#ShippingCountry").val();
        var pList = [];
        listItems = $("#list").find("li").each(function(){
                pQty = $(this).find('#quantity').val();
        	var product = {
                        id: $(this).find("#product_id").val(),
                        qty: pQty,
                        msg: buyer_comment,
                        buyerofferprice: offerprice,
                        shipping_country: shipping_country,
        	};
        	if(pQty > 0) {
                	pList.push(product);
        	}
    	});
    	var p = {
                products_chosen: pList,
    	}
    	if (pList.length == 0) {
        	alert("Please update the quantity of the products selected");
    	}
    	else {
        	$.ajaxSetup({
                	type: 'POST',
            		dataType: "json",
                	timeout: 30000,
                	beforeSend: function(xhr, settings) {
                        	if (!this.crossDomain) {
                                	xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
                        	}
                	},
                	error: function(xhr) {
                        	//alert('Failed to send offer: ' + xhr.status + ' ' + xhr.statusText);
               		}
        	})
        	$.post("/nameyourprice/buyermakeoffer/", p, function(d) {
            		var e;
            		var i = true;
            		if (!d) {
                		e = "Unexpected error, please try again later."
            		} else {
                            window.location = "/nameyourprice/makeoffer/";
                            return true
            		}
		})

        }
    });
    $(document).on("submit", ".PaypalForm", function(b) {
        b.preventDefault();
  	total_amt_due = $(".PaypalForm").find("input[name=total_amt_due]").val();
  	shipping_description = $(".PaypalForm").find("input[name=shipping_description]").val();
  	shipping_method_name = $(".PaypalForm").find("input[name=shipping_method_name]").val();
  	shipping_charge = $(".PaypalForm").find("input[name=shipping_charge]").val();
  	promotion_code = $(".PaypalForm").find("input[name=promotion_code]").val();
  	discount = $(".PaypalForm").find("input[name=discount]").val();
  	payment_type = $(".PaypalForm").find("input[name=payment_type]").val();
	var data = {
		total_amt_due: total_amt_due,
		shipping_description: shipping_description,
		shipping_method_name: shipping_method_name,
		shipping_charge: shipping_charge,
		promotion_code: promotion_code,
		discount: discount,
		payment_type: payment_type,
	}
        	$.ajaxSetup({
                	type: 'POST',
            		dataType: "json",
                	timeout: 30000,
                	beforeSend: function(xhr, settings) {
                        	if (!this.crossDomain) {
                                	xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
                        	}
                	},
                	error: function(xhr) {
                        	// alert('Failed to send offer: ' + xhr.status + ' ' + xhr.statusText);
               		}
        	})
        	$.post("/checkout/checkout_payment/", data, function(d) {
            		var e;
            		var i = true;
            		if (!d) {
                		e = "Unexpected error, please try again later."
            		} else {
                            document.location.href = d.paypal_url;
                            return true
            		}
		})

    });
    $(document).on("submit", ".ChangePasswordForm", function(b) {
        b.preventDefault();
  	old_password = $(".ChangePasswordForm").find("input[name=old_password]").val();
  	new_password_1 = $(".ChangePasswordForm").find("input[name=new_password1]").val();
  	new_password_2 = $(".ChangePasswordForm").find("input[name=new_password2]").val();
	var data = {
		old_password: old_password,
		new_password1: new_password_1,
		new_password2: new_password_2,
	}
        	$.ajaxSetup({
                	type: 'POST',
            		dataType: "json",
                	timeout: 30000,
                	beforeSend: function(xhr, settings) {
                        	if (!this.crossDomain) {
                                	xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
                        	}
                	},
                	error: function(xhr) {
				response = xhr.responseText;
				if (response.indexOf("incorrectly") != -1) {
					alert("Incorrect old password");
				}
				else {
					if (response.indexOf("match") != -1) {
						alert("The two new password fields do not match");
					}
					else {
						$(".password_change_done").show();
						$(".afterpasswordchange").trigger("collapse");
					}
				}
               		}
        	})
        	$.post("/accounts/password_change/", data, function(d) {
            		var e;
            		var i = true;
            		if (!d) {
				alert(d);
                		e = "Unexpected error, please try again later."
            		} else {
                            document.location.href = "/accounts/password_change/done/";
                            return true
            		}
		})

    });
/*
    $(document).on("pageshow", "[data-role=page]", function(b, c) {
        try {
            _gaq.push(["_setAccount", "UA-37084333-1"]);
            hash = location.hash;
            if (hash) {
                _gaq.push(["_trackPageview", hash.substr(1)])
            } else {
                _gaq.push(["_trackPageview"])
            }
        } catch (a) {}
    });
    _gaq.push(["_setAccount", "UA-37084333-1"]);
    _gaq.push(["_trackPageview"])
*/
});
function changeCountry(b, e, d) {
    if (!b) {
        return
    }
    var a = $("#" + e + "_fieldset");
    var c = $("#" + d + "_fieldset");
    var f = b[b.selectedIndex].value;
    $("#" + e).selectmenu("refresh");
    if ("USA" == f) {
        c.hide();
        $("#" + d).val("");
        a.show()
    } else {
        c.show();
        a.hide();
        $("#" + e).val("")
    }
}

function replaceSubmitButton(a, c) {
    var b = document.createElement("input");
    b.type = "button";
    b.id = a.id;
    b.value = a.value;
    b.className = a.className;
    b.setAttribute("data-icon", a.getAttribute("data-icon"));
    b.setAttribute("data-theme", a.getAttribute("data-theme"));
    a.parentNode.replaceChild(b, a);
    $(b).bind("click", c);
    return b
}

function simpleFormSubmitConfirm(b, c, a) {
    $(b).simpledialog2({
        mode: "button",
        headerClose: false,
        buttonPrompt: c,
        headerText: a,
        buttons: {
            OK: {
                click: function() {
                    b.submit()
                }
            },
            Cancel: {
                click: function() {
                    return true
                },
                icon: "delete",
                theme: "c"
            }
        }
    })
}

function doRotateMain(a) {
    rotIndex = rotIndex + a;
    if (rotIndex < 0) {
        rotIndex = rotSize - 1
    } else {
        if (rotIndex >= rotSize) {
            rotIndex = 0
        }
    }
    document.rotateImage.src = rotImages[rotIndex];
    $("#categoryTitle .ui-btn-text").text(rotTitle[rotIndex])
}

function doRotatingMainLink() {
    document.location.href = rotHrefs[rotIndex]
}

function enableQtyIfFeaturesSelected(b, d) {
    var c = $("#" + d);
    var a = true;
    $("select." + b).each(function(e) {
        if (this.options.selectedIndex == 0) {
            a = false
        }
    });
    if (a) {
        c.selectmenu("enable");
        if (c.val() == "0") {
            c.val("1");
            c.selectmenu("refresh")
        }
    } else {
        c.selectmenu("disable")
    }
}

function scrollToFirst(a, e) {
    var c = $.mobile.activePage[0];
    if (c) {
        var b = $(c).find(a);
        var d = 0;
        if (e) {
            d = e
        }
        if (b) {
            var e = b.offset();
            if (e && e.top) {
                $.mobile.silentScroll(b.offset().top + d)
            }
        }
    }
}

function showShoppingBagSize(b) {
    if (b) {
        var a = $(".cartSize");
        if (a) {
            a.html(b);
            if (b > 9) {
                a.css("margin-left", "0px")
            } else {
                a.css("margin-left", "3px")
            }
        }
    }
}

function rotateImages(c, d, a, b) {
    a.val = a.val + c;
    if (a.val < 0) {
        a.val = d.length - 1
    } else {
        if (a.val >= d.length) {
            a.val = 0
        }
    }
    rotateImagesTo(a.val, d, a, b)
}

function rotateImagesTo(e, c, a, b) {
    var d = $("#" + b);
    if (d) {
        $(".main-category-image-swipable .ui-loader").show();
        d.attr("src", c[e]);
        d.load(function() {
            $(".main-category-image-swipable .ui-loader").hide()
        })
    }
    $("#slider-" + b + " .dot").removeClass("selected");
    $("#dot-" + b + "_" + e).addClass("selected")
}

function rotateMainCategoryImageTo(a, b) {
    rotateImagesTo(a, window["addImages" + b], window["imageIndex" + b], "main-category-image" + b)
}

function rotateMainCategoryImageLeft(a) {
    rotateImages(-1, window["addImages" + a], window["imageIndex" + a], "main-category-image" + a)
}

function rotateMainCategoryImageRight(a) {
    rotateImages(1, window["addImages" + a], window["imageIndex" + a], "main-category-image" + a)
}

function showLargerImage(c, a, d) {
    var b = $("#" + d).attr("action");
    $("#" + d).attr("action", b + "?largeImageLink=" + c[a.val]);
    $("#" + d).submit()
}

function toggleSearchPanel() {
// we have to use class; since jquery mobile would bring in multiple divs with the same ids
	$(".search-panel").toggle();
	$("[data-role=panel]").panel("close");
}

var allproducts = $.jStorage.get("allproducts");
var localList4Search = $.jStorage.get("list4Search");
var localList4Offers = $.jStorage.get("list4Offers");
function getAllProducts(c) {

     if (localList4Search == null || localList4Offers == null) {
        $.ajaxSetup({
                type: 'GET',
                timeout: 30000,
                error: function(xhr) {
                        console.log('We are debugging our mobile shop, please continue to use our desktop platform until our mobile shop is complete: ' + xhr.status + ' ' + xhr.statusText);
			console.log('response: ' + xhr.responseText);
               }
        })

	//base_url = window.location.origin;
	//c = base_url + c;
	console.log("getAllProducts: " + c);
        $.ajax({
            url: c,
            type: "GET",
            dataType: "json",
            crossDomain: true,
        }).then(function(g) {
		console.log("Get all products");
		allproducts = g;
		console.log("Loading allproducts into storage: size = " + $.jStorage.storageSize());
		$.jStorage.set("allproducts",g, {TTL:3600000});
		console.log("Loaded allproducts into storage: size = " + $.jStorage.storageSize());
 	    	localList4Search = "";
              	$.each( g, function ( i, val ) {
                    localList4Search += "<li><a class='searchItem' id='searchItem" + i + "' href='#'>" + val.name + "</a></li>";
              	});
		$.jStorage.set("list4Search",localList4Search, {TTL:3600000});
 	    	localList4Offers = "";
        	$.each(g, function(h, j) {
			localList4Offers += '<li product-id="' + j.id + '" ';
			localList4Offers += 'product-name="' + j.name + '" ';
			localList4Offers += 'sale-price="' + j.sale_price + '" ';
			localList4Offers += '>';
			localList4Offers += '<input type="hidden" class="product_id" value="' + j.id + '" />';
			localList4Offers += '<input type="hidden" class="sale_price" value="' + j.sale_price + '" />';
                	localList4Offers += '<a class="searchItem" id="searchItem' + h + '" href="#">' + j.name + '</a></li>'
            	});
		$.jStorage.set("list4Offers",localList4Offers, {TTL:3600000});
	})
    }

}

function prepopulateSearchList(a) {
       var $ul = a;
              $ul.html( localList4Search );
            $ul.listview("refresh");
            $ul.trigger("updatelayout");
            $(".searchItem").click(function() {
                f.val($(this).text());
                $("#aa-search-input").val($(this).text());
            })
}
function productAutocomplete(a, e) {
    var f = $(e.input),
        d = f.val(),
        b = "";
    a.html("");
    $("#aa-search-input").val(f.val());
    if (d && d.length > 2) {
        a.html("<li><div class='ui-loader'><span class='ui-icon ui-icon-loading'></span></div></li>");
        a.listview("refresh");
        a.show();
        $.each(allproducts, function(h, j) {
                b += "<li><a class='searchItem' id='searchItem" + h + "' href='#'>" + j.name + "</a></li>"
            });
            a.html(b);
            a.listview("refresh");
            a.trigger("updatelayout");
            $(".searchItem").click(function() {
                f.val($(this).text());
                $("#aa-search-input").val($(this).text());
                a.hide()
            })
    }
}

function productAutoComplete(a, data) {
       var $ul = a,
       $input = $( data.input ),
       value = $input.val(),
       html = "";
       $ul.html( "" );
       $("#aa-search-input").val(value);
       if ( value && value.length > 2 ) {
              $ul.html( "<li><div class='ui-loader'><span class='ui-icon ui-icon-loading'></span></div></li>" );
              $ul.listview( "refresh" );
              $ul.html( localList4Search );
              $ul.listview( "refresh" );
              $ul.trigger( "updatelayout");
            $(".searchItem").click(function() {
                $input.val($(this).text());
                $("#aa-search-input").val($(this).text());
                a.hide()
            })
       }
}

function products4MakeOffer(a, e) {
    var f = $(e.input),
        d = f.val(),
        b = "";
    a.html("");
    $("#make-offer-input").val(f.val());
    if (d && d.length > 2) {
        a.html("<li><div class='ui-loader'><span class='ui-icon ui-icon-loading'></span></div></li>");
        a.listview("refresh");
        a.show();
        $.each(allproducts, function(h, j) {
		b += '<li product-id="' + j.id + '" ';
		b += 'product-name="' + j.name + '" ';
		b += 'sale-price="' + j.price + '" ';
		b += '>';
		b += '<input type="hidden" class="product_id" value="' + j.id + '" />';
		b += '<input type="hidden" class="sale_price" value="' + j.price + '" />';
                b += '<a class="searchItem" id="searchItem' + h + '" href="#">' + j.name + '</a></li>'
            });
            a.html(b);
            a.listview("refresh");
            a.trigger("updatelayout");
            $(".searchItem").click(function() {
                f.val($(this).text());
                $("#make-offer-input").val($(this).text());
                a.hide()
            })
    	$('#productList').children('li').bind('click', function(e) {
		var pId = $(this).attr('product-id');
		var pName = $(this).attr('product-name');
		var pSalePrice = $(this).attr('sale-price');
		add2Offer(pId, pName, pSalePrice, 1);
	});
    }
}

var listCreated = false;
function add2Offer(productId, productName, sale_price, qty) {
    //Create the listview if not created
    if(!listCreated){
          $("#offerbasket").append("<ul id='list' data-role='listview' data-inset='true'></ul>");
          listCreated = true;
          $("#offerbasket").trigger("create");
	  $("#empty").remove();
    }
    var html = "<li><h3>" + productName + "</h3>";
    html += "<div class='ui-grid-a' id='grid'>";
    html += "<div class='ui-block-a' style='width:60%;padding-top:10px;'>";
    html += "<p>Sale Price: $" + sale_price + "</p>";
    html += "</div>";
    html += "<div class='ui-block-b' style='width:40%;padding-top:10px;'>";
    html += "<input type='hidden' value='"+ productId +"' id='product_id' />";
    html += "<input type='hidden' value='"+ sale_price +"' id='sale_price' />";
    html += "<p>Qty: <input type='number' name='quantity' value='" + qty +"' id='quantity' style='width: 30px !important;' onchange='calculateTotal()' onkeypress='return isNumber(event);' /></p>";
    html += "</div>";
    html += "</div>";
    html += "</li>";
    $("#list").append(html);
    $("#list").listview("refresh");
    $("#buyitnowbox").css("display", "block");
    $("#offerbox").css("display", "block");

    $('input[data-type="search"]').val("");
    $('.OfferBoxHeader').find('h3').text("Add more ?");

    calculateTotal();

}

function calculateTotal() {
	total_qty = 0;
	total_price = 0;
	listItems = $("#list").find("li").each(function(){
		product = $(this);
		qty = product.find('#quantity').val();
		sale_price = product.find('#sale_price').val();
		total_price += sale_price * qty;
		$(".BuyItNowPrice").text("$" + total_price);
		$("#offerprice").val(total_price);
		total_qty += parseInt(qty);
	});
	a = $(".offercount");
	if (a) {
		a.html(" (count: " + total_qty + ")");
	}

}


function updateShoppingCartSize(c) {
	//base_url = window.location.origin;
	//c = base_url + c;
	console.log("updateShoppingCartSize: " + c);
        $.ajax({
            url: c,
            type: "GET",
            dataType: "json",
            crossDomain: true,
        }).then(function(g) {
		showShoppingBagSize(g.cartSize);
	})

}

function getProductAutocomplete(a, c, e) {
    var f = $(e.input),
        d = f.val(),
        b = "";
    a.html("");
    $("#aa-search-input").val(f.val());
    if (d && d.length > 2) {
        a.html("<li><div class='ui-loader'><span class='ui-icon ui-icon-loading'></span></div></li>");
        a.listview("refresh");
        a.show();
	base_url = window.location.origin;
	c = base_url + c;
	console.log("getProductAutoComplete: " + c);
        $.ajax({
            url: c,
            type: "POST",
            dataType: "json",
            crossDomain: true,
            data: {
                keywords: f.val()
            }
        }).then(function(g) {
            $.each(g, function(h, j) {
                b += "<li><a class='searchItem' id='searchItem" + h + "' href='#'>" + j.keyword + "</a></li>"
            });
            a.html(b);
            a.listview("refresh");
            a.trigger("updatelayout");
            $(".searchItem").click(function() {
                f.val($(this).text());
                $("#aa-search-input").val($(this).text());
                a.hide()
            })
        })
    }
}

function clickclear(b, a) {
    if (b.value == a) {
        b.value = ""
    }
}

function clickrecall(b, a) {
    if (b.value == "") {
        b.value = a
    }
}

function validateEmailSubmit(d, c) {
    var b = d.parents("form:first");
    var e = b.find(".inputBox:first");
    var a = validateEmail(e.val(), c);
    return a
}

function validateEmail(a, c) {
    var b = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
    if (b.test(a)) {
        return true
    }
    if (c) {
        alert(c)
    }
    console.log("not a valid email: ", a);
    return false
}

function activateSubmitIfValidEmail(d, c, e) {
    var a = d.val();
    var b = false;
    if (d && d.parent() && d.parent().hasClass("ui-input-text")) {
        b = d.parent()
    }
    if (validateEmail(a)) {
        if (b) {
            b.removeClass("error")
        } else {
            d.removeClass("error")
        }
        if (c) {
            c.removeClass("disabled");
            c.attr("disabled", "");
            c.removeAttr("disabled")
        }
        if (d.form) {
            d.form._invalid = false
        }
    } else {
        if (!e || e != a) {
            if (b) {
                b.addClass("error")
            } else {
                d.addClass("error")
            }
        } else {
            if (b) {
                b.removeClass("error")
            } else {
                d.removeClass("error")
            }
        }
        if (c) {
            c.addClass("disabled");
            c.addClass("disabled");
            c.attr("disabled", "disabled")
        }
        if (d.form) {
            d.form._invalid = true
        }
    }
}

function activateSubmitIfValidEmailRecallDefault(b, a, c) {
    clickrecall(b, c);
    activateSubmitIfValidEmail(b, a, c)
}

function pinIt() {
    var a = document.createElement("script");
    a.setAttribute("type", "text/javascript");
    a.setAttribute("charset", "UTF-8");
    a.setAttribute("src", "/static/mobile/js/pinmarklet.js?r=" + (Math.random() * 99999999));
    document.body.appendChild(a)
}

function share(a, b) {
    $(document).simpledialog2({
        mode: "blank",
        headerClose: false,
        blankContent: "<a data-role='button' data-icon='check' data-rel='dialog' href='http://www.facebook.com/sharer.php?u=" + a + "&amp;t=" + b + "' target='_blank'>Facebook</a><a data-role='button' data-icon='check' href='http://twitter.com/home?status=" + b + " " + a + "' target='_blank'>Twitter</a><a data-role='button' data-icon='check' data-rel='dialog' href='javascript: pinIt();'>Pin It</a><a rel='close' data-role='button' data-theme='c' data-icon='delete' href='#'>Close</a>"
    })
};

function addAddressWrapper() {
	$('#id_shipping_name').parent().parent().prepend('<div class="ui-body ui-body-c ui-corner-all"><b>SHIPPING ADDRESS<b>');
	$('#id_billing_name').parent().parent().prepend('</div><div class="ui-body ui-body-c ui-corner-all"><b>BILLING ADDRESS<b>');
	$('#id_billing_zip').parent().parent().append('</div>');
};

function shipsame(){
        if($("#sameasshipping").is(":checked")){
             $("#id_billing_name").val($("#id_shipping_name").val());
             $("#id_billing_address_1").val($("#id_shipping_address_1").val());
             $("#id_billing_address_2").val($("#id_shipping_address_2").val());
             $("#id_billing_city").val($("#id_shipping_city").val());
             $("#id_billing_state").val($("#id_shipping_state").val());
             $("#id_billing_country").val($("#id_shipping_country").val());
             $("#id_billing_zip").val($("#id_shipping_zip").val());

         }else{


        }
};

function ConfirmCancelOffer(bid, comment) {

     $.ajaxSetup({
             type: 'POST',
             timeout: 30000,
             beforeSend: function(xhr, settings) {
                  if (!this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
                  }
             },
             error: function(xhr) {
                  // alert('Error: ' + xhr.status + ' ' + xhr.statusText);
             }
     })

     var bid = {
            b_id: bid,
            comment: comment,
     };
     jQuery.post("/nameyourprice/cancelyouroffer/", bid,
           function(response){
                 // evaluate the "success" parameter
                if(response.success == "True"){
                // disable the submit button to prevent duplicates
                //jQuery("#SellerOffer").html(response.html).slideDown();
                $("#CancelOffer").hide();
                $("#CancelOfferForm").hide();
                $("#CancelOffer").hide();
                $("#CancelOfferForm").hide();
                if(response.open_offer_count == 0){
                      $("#errorMsg").hide();
                }
                else{
                      $("#offer_count").text(response.open_offer_count);
                }

         }
         else{
         }
     }, "json");

}

function ConfirmCounterOffer(bid, price, comment) {

     $.ajaxSetup({
             type: 'POST',
             timeout: 30000,
             beforeSend: function(xhr, settings) {
                  if (!this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
                  }
             },
             error: function(xhr) {
                  // alert('Error: ' + xhr.status + ' ' + xhr.statusText);
             }
     })


        var bid = {
                b_id: bid,
                price: price,
                comment: comment,
        };
        jQuery.post("/nameyourprice/buyercounteryouroffer/", bid,
                function(response){
                        // evaluate the "success" parameter
                        if(response.success == "True"){
                        // disable the submit button to prevent duplicates
				return true;
                        }
                        else{
				return false;
                        }
                }, "json");


}

function ConfirmDeclineOffer(bid, comment) {
     $.ajaxSetup({
             type: 'POST',
             timeout: 30000,
             beforeSend: function(xhr, settings) {
                  if (!this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
                  }
             },
             error: function(xhr) {
                  // alert('Error: ' + xhr.status + ' ' + xhr.statusText);
             }
     })


        var bid = {
                b_id: bid,
                comment: comment,
        };
        jQuery.post("/nameyourprice/declineyouroffer/", bid,
                function(response){
                        // evaluate the "success" parameter
                        if(response.success == "True"){
                        // disable the submit button to prevent duplicates
                        }
                        else{
                        }
                }, "json");


}
function SubscribeNewsletter(email) {
     $.ajaxSetup({
             type: 'POST',
             timeout: 30000,
             beforeSend: function(xhr, settings) {
                  if (!this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
                  }
             },
             error: function(xhr) {
                  //alert('Error: ' + xhr.status + ' ' + xhr.statusText);
             }
     })

        var data = {
                email: email,
        };

        jQuery.post("/mobile/email_signup/", data,
                function(response){
                        // evaluate the "success" parameter
                        if(response.success == "True"){
                        // disable the submit button to prevent duplicates
                        }
                        else{
                        }
                }, "json");


}
function Password_Reset(email) {
     $.ajaxSetup({
             type: 'POST',
             timeout: 30000,
             beforeSend: function(xhr, settings) {
                  if (!this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
                  }
             },
             error: function(xhr) {
		  if (xhr.status == 200) {
			response = xhr.responseText;
			if (response.indexOf("successful") == -1) {
				alert("Please enter a valid email address");
			}
			else {
				$(".password_reset_done").show();
			}
		  }
             }
     })

        var data = {
                email: email,
        };

        jQuery.post("/accounts/password_reset/", data,
                function(response){
                        // evaluate the "success" parameter
                        if(response.success == "True"){
                        // disable the submit button to prevent duplicates
                        }
                        else{
                        }
                }, "json");


}
