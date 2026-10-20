<?xml version="1.0" encoding="utf-8"?>

<!-- ======================================================== -->
<!-- File    : alternative.xsl                                -->
<!-- Content : PM2 LaTeX XSLT for the alternatives of a       -->
<!--           Business Case                                  -->
<!-- Author  : Amador Durán Toro & Claude Code                -->
<!-- Date    : 2026/10/20                                     -->
<!-- Version : 1.0                                            -->
<!-- ======================================================== -->
<!-- The chosen alternative is marked in the header instead   -->
<!-- of a row; the SWOT properties are ordinary rows.         -->
<!-- ======================================================== -->

<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:proteus="http://proteus.us.es"
  xmlns:proteus-utils="http://proteus.us.es/utils"
>

  <xsl:template
    match="object[contains(concat(' ', normalize-space(@classes), ' '),' alternative ')]"
    name="alternative_template"
    priority="1"
  >
    <xsl:variable name="postfix">
      <xsl:if test="properties/booleanProperty[@name='chosen'] = 'true'">
        <xsl:value-of select="proteus-utils:i18n('xslt.chosen')"/>
      </xsl:if>
    </xsl:variable>

    <xsl:call-template name="generate_table">
      <xsl:with-param name="postfix" select="string($postfix)"/>
      <xsl:with-param name="excluded_properties"
        select="',:Proteus-name,:Proteus-code,:Proteus-date,version,authors,sources,chosen,'"/>
    </xsl:call-template>
  </xsl:template>

</xsl:stylesheet>
