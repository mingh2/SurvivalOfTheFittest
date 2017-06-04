//
// This file was generated by the JavaTM Architecture for XML Binding(JAXB) Reference Implementation, v2.2.4 
// See <a href="http://java.sun.com/xml/jaxb">http://java.sun.com/xml/jaxb</a> 
// Any modifications to this file will be lost upon recompilation of the source schema. 
// Generated on: 2017.06.04 at 04:39:59 PM PDT 
//


package com.microsoft.Malmo.Schemas;

import java.math.BigDecimal;
import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlAttribute;
import javax.xml.bind.annotation.XmlType;


/**
 * 
 *             Specify an entity by location and type.
 *         
 * 
 * <p>Java class for DrawEntity complex type.
 * 
 * <p>The following schema fragment specifies the expected content contained within this class.
 * 
 * <pre>
 * &lt;complexType name="DrawEntity">
 *   &lt;complexContent>
 *     &lt;extension base="{http://ProjectMalmo.microsoft.com}DrawObjectType">
 *       &lt;attribute name="x" use="required" type="{http://www.w3.org/2001/XMLSchema}decimal" />
 *       &lt;attribute name="y" use="required" type="{http://www.w3.org/2001/XMLSchema}decimal" />
 *       &lt;attribute name="z" use="required" type="{http://www.w3.org/2001/XMLSchema}decimal" />
 *       &lt;attribute name="type" use="required" type="{http://ProjectMalmo.microsoft.com}SpawnableTypes" />
 *       &lt;attribute name="yaw" type="{http://www.w3.org/2001/XMLSchema}decimal" default="0" />
 *       &lt;attribute name="pitch" type="{http://www.w3.org/2001/XMLSchema}decimal" default="0" />
 *       &lt;attribute name="xVel" type="{http://www.w3.org/2001/XMLSchema}decimal" default="0" />
 *       &lt;attribute name="yVel" type="{http://www.w3.org/2001/XMLSchema}decimal" default="0" />
 *       &lt;attribute name="zVel" type="{http://www.w3.org/2001/XMLSchema}decimal" default="0" />
 *     &lt;/extension>
 *   &lt;/complexContent>
 * &lt;/complexType>
 * </pre>
 * 
 * 
 */
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "DrawEntity")
public class DrawEntity
    extends DrawObjectType
{

    @XmlAttribute(name = "x", required = true)
    protected BigDecimal x;
    @XmlAttribute(name = "y", required = true)
    protected BigDecimal y;
    @XmlAttribute(name = "z", required = true)
    protected BigDecimal z;
    @XmlAttribute(name = "type", required = true)
    protected SpawnableTypes type;
    @XmlAttribute(name = "yaw")
    protected BigDecimal yaw;
    @XmlAttribute(name = "pitch")
    protected BigDecimal pitch;
    @XmlAttribute(name = "xVel")
    protected BigDecimal xVel;
    @XmlAttribute(name = "yVel")
    protected BigDecimal yVel;
    @XmlAttribute(name = "zVel")
    protected BigDecimal zVel;

    /**
     * Gets the value of the x property.
     * 
     * @return
     *     possible object is
     *     {@link BigDecimal }
     *     
     */
    public BigDecimal getX() {
        return x;
    }

    /**
     * Sets the value of the x property.
     * 
     * @param value
     *     allowed object is
     *     {@link BigDecimal }
     *     
     */
    public void setX(BigDecimal value) {
        this.x = value;
    }

    /**
     * Gets the value of the y property.
     * 
     * @return
     *     possible object is
     *     {@link BigDecimal }
     *     
     */
    public BigDecimal getY() {
        return y;
    }

    /**
     * Sets the value of the y property.
     * 
     * @param value
     *     allowed object is
     *     {@link BigDecimal }
     *     
     */
    public void setY(BigDecimal value) {
        this.y = value;
    }

    /**
     * Gets the value of the z property.
     * 
     * @return
     *     possible object is
     *     {@link BigDecimal }
     *     
     */
    public BigDecimal getZ() {
        return z;
    }

    /**
     * Sets the value of the z property.
     * 
     * @param value
     *     allowed object is
     *     {@link BigDecimal }
     *     
     */
    public void setZ(BigDecimal value) {
        this.z = value;
    }

    /**
     * Gets the value of the type property.
     * 
     * @return
     *     possible object is
     *     {@link SpawnableTypes }
     *     
     */
    public SpawnableTypes getType() {
        return type;
    }

    /**
     * Sets the value of the type property.
     * 
     * @param value
     *     allowed object is
     *     {@link SpawnableTypes }
     *     
     */
    public void setType(SpawnableTypes value) {
        this.type = value;
    }

    /**
     * Gets the value of the yaw property.
     * 
     * @return
     *     possible object is
     *     {@link BigDecimal }
     *     
     */
    public BigDecimal getYaw() {
        if (yaw == null) {
            return new BigDecimal("0");
        } else {
            return yaw;
        }
    }

    /**
     * Sets the value of the yaw property.
     * 
     * @param value
     *     allowed object is
     *     {@link BigDecimal }
     *     
     */
    public void setYaw(BigDecimal value) {
        this.yaw = value;
    }

    /**
     * Gets the value of the pitch property.
     * 
     * @return
     *     possible object is
     *     {@link BigDecimal }
     *     
     */
    public BigDecimal getPitch() {
        if (pitch == null) {
            return new BigDecimal("0");
        } else {
            return pitch;
        }
    }

    /**
     * Sets the value of the pitch property.
     * 
     * @param value
     *     allowed object is
     *     {@link BigDecimal }
     *     
     */
    public void setPitch(BigDecimal value) {
        this.pitch = value;
    }

    /**
     * Gets the value of the xVel property.
     * 
     * @return
     *     possible object is
     *     {@link BigDecimal }
     *     
     */
    public BigDecimal getXVel() {
        if (xVel == null) {
            return new BigDecimal("0");
        } else {
            return xVel;
        }
    }

    /**
     * Sets the value of the xVel property.
     * 
     * @param value
     *     allowed object is
     *     {@link BigDecimal }
     *     
     */
    public void setXVel(BigDecimal value) {
        this.xVel = value;
    }

    /**
     * Gets the value of the yVel property.
     * 
     * @return
     *     possible object is
     *     {@link BigDecimal }
     *     
     */
    public BigDecimal getYVel() {
        if (yVel == null) {
            return new BigDecimal("0");
        } else {
            return yVel;
        }
    }

    /**
     * Sets the value of the yVel property.
     * 
     * @param value
     *     allowed object is
     *     {@link BigDecimal }
     *     
     */
    public void setYVel(BigDecimal value) {
        this.yVel = value;
    }

    /**
     * Gets the value of the zVel property.
     * 
     * @return
     *     possible object is
     *     {@link BigDecimal }
     *     
     */
    public BigDecimal getZVel() {
        if (zVel == null) {
            return new BigDecimal("0");
        } else {
            return zVel;
        }
    }

    /**
     * Sets the value of the zVel property.
     * 
     * @param value
     *     allowed object is
     *     {@link BigDecimal }
     *     
     */
    public void setZVel(BigDecimal value) {
        this.zVel = value;
    }

}
