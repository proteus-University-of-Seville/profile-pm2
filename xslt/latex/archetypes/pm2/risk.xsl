<?xml version="1.0" encoding="utf-8"?>

<!-- ======================================================== -->
<!-- File    : risk.xsl                                       -->
<!-- Content : PM2 LaTeX XSLT for risks                       -->
<!-- Author  : Amador Durán Toro & Claude Code                -->
<!-- Date    : 2026/10/19                                     -->
<!-- Version : 1.0                                            -->
<!-- ======================================================== -->
<!-- Same as the HTML module: the header shows the risk level -->
<!-- (likelihood x impact) once both have been assessed, and  -->
<!-- the escalation is only shown when it is required.        -->
<!-- ======================================================== -->

<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:proteus="http://proteus.us.es"
  xmlns:proteus-utils="http://proteus.us.es/utils"
>

  <!-- Numeric value (1 to 5) of a likelihood or impact level, 0 if tbd -->
  <xsl:template name="risk_level_value">
    <xsl:param name="level"/>
    <xsl:choose>
      <xsl:when test="$level = 'very-low'">1</xsl:when>
      <xsl:when test="$level = 'low'">2</xsl:when>
      <xsl:when test="$level = 'medium'">3</xsl:when>
      <xsl:when test="$level = 'high'">4</xsl:when>
      <xsl:when test="$level = 'very-high'">5</xsl:when>
      <xsl:otherwise>0</xsl:otherwise>
    </xsl:choose>
  </xsl:template>

  <xsl:template
    match="object[contains(concat(' ', normalize-space(@classes), ' '),' risk ')]"
    name="risk_template"
    priority="1"
  >
    <xsl:variable name="likelihood">
      <xsl:call-template name="risk_level_value">
        <xsl:with-param name="level" select="normalize-space(properties/enumProperty[@name='likelihood'])"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:variable name="impact">
      <xsl:call-template name="risk_level_value">
        <xsl:with-param name="level" select="normalize-space(properties/enumProperty[@name='impact'])"/>
      </xsl:call-template>
    </xsl:variable>

    <xsl:variable name="postfix">
      <xsl:if test="$likelihood * $impact > 0">
        <xsl:value-of select="proteus-utils:i18n('xslt.risk_level', string($likelihood * $impact))"/>
      </xsl:if>
    </xsl:variable>

    <xsl:variable name="excluded">
      <xsl:text>,:Proteus-name,:Proteus-code,:Proteus-date,version,authors,sources,</xsl:text>
      <xsl:if test="properties/booleanProperty[@name='escalation'] != 'true'">escalation,</xsl:if>
    </xsl:variable>

    <xsl:call-template name="generate_table">
      <xsl:with-param name="postfix" select="string($postfix)"/>
      <xsl:with-param name="excluded_properties" select="string($excluded)"/>
    </xsl:call-template>
  </xsl:template>

</xsl:stylesheet>
