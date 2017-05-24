//
// This file was generated by the JavaTM Architecture for XML Binding(JAXB) Reference Implementation, v2.2.4 
// See <a href="http://java.sun.com/xml/jaxb">http://java.sun.com/xml/jaxb</a> 
// Any modifications to this file will be lost upon recompilation of the source schema. 
// Generated on: 2017.05.23 at 10:54:06 AM PDT 
//


package com.microsoft.Malmo.Schemas;

import java.math.BigDecimal;
import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlAttribute;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlType;


/**
 * <p>Java class for anonymous complex type.
 * 
 * <p>The following schema fragment specifies the expected content contained within this class.
 * 
 * <pre>
 * &lt;complexType>
 *   &lt;complexContent>
 *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *       &lt;attGroup ref="{http://ProjectMalmo.microsoft.com}RewardProducerAttributes"/>
 *       &lt;attribute name="initialReward" use="required" type="{http://www.w3.org/2001/XMLSchema}decimal" />
 *       &lt;attribute name="delta" use="required" type="{http://www.w3.org/2001/XMLSchema}decimal" />
 *       &lt;attribute name="density" use="required" type="{http://ProjectMalmo.microsoft.com}RewardDensityForTimeTaken" />
 *       &lt;attribute name="rewardDistribution" type="{http://www.w3.org/2001/XMLSchema}string" default="" />
 *     &lt;/restriction>
 *   &lt;/complexContent>
 * &lt;/complexType>
 * </pre>
 * 
 * 
 */
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "")
@XmlRootElement(name = "RewardForTimeTaken")
public class RewardForTimeTaken {

    @XmlAttribute(name = "initialReward", required = true)
    protected BigDecimal initialReward;
    @XmlAttribute(name = "delta", required = true)
    protected BigDecimal delta;
    @XmlAttribute(name = "density", required = true)
    protected RewardDensityForTimeTaken density;
    @XmlAttribute(name = "rewardDistribution")
    protected String rewardDistribution;
    @XmlAttribute(name = "dimension")
    protected Integer dimension;

    /**
     * Gets the value of the initialReward property.
     * 
     * @return
     *     possible object is
     *     {@link BigDecimal }
     *     
     */
    public BigDecimal getInitialReward() {
        return initialReward;
    }

    /**
     * Sets the value of the initialReward property.
     * 
     * @param value
     *     allowed object is
     *     {@link BigDecimal }
     *     
     */
    public void setInitialReward(BigDecimal value) {
        this.initialReward = value;
    }

    /**
     * Gets the value of the delta property.
     * 
     * @return
     *     possible object is
     *     {@link BigDecimal }
     *     
     */
    public BigDecimal getDelta() {
        return delta;
    }

    /**
     * Sets the value of the delta property.
     * 
     * @param value
     *     allowed object is
     *     {@link BigDecimal }
     *     
     */
    public void setDelta(BigDecimal value) {
        this.delta = value;
    }

    /**
     * Gets the value of the density property.
     * 
     * @return
     *     possible object is
     *     {@link RewardDensityForTimeTaken }
     *     
     */
    public RewardDensityForTimeTaken getDensity() {
        return density;
    }

    /**
     * Sets the value of the density property.
     * 
     * @param value
     *     allowed object is
     *     {@link RewardDensityForTimeTaken }
     *     
     */
    public void setDensity(RewardDensityForTimeTaken value) {
        this.density = value;
    }

    /**
     * Gets the value of the rewardDistribution property.
     * 
     * @return
     *     possible object is
     *     {@link String }
     *     
     */
    public String getRewardDistribution() {
        if (rewardDistribution == null) {
            return "";
        } else {
            return rewardDistribution;
        }
    }

    /**
     * Sets the value of the rewardDistribution property.
     * 
     * @param value
     *     allowed object is
     *     {@link String }
     *     
     */
    public void setRewardDistribution(String value) {
        this.rewardDistribution = value;
    }

    /**
     * Gets the value of the dimension property.
     * 
     * @return
     *     possible object is
     *     {@link Integer }
     *     
     */
    public int getDimension() {
        if (dimension == null) {
            return  0;
        } else {
            return dimension;
        }
    }

    /**
     * Sets the value of the dimension property.
     * 
     * @param value
     *     allowed object is
     *     {@link Integer }
     *     
     */
    public void setDimension(Integer value) {
        this.dimension = value;
    }

}
