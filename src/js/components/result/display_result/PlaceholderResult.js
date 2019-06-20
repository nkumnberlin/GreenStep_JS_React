import React, {Fragment} from 'react'
import {Segment, Container, Image, Step, Header, Icon, Loader} from 'semantic-ui-react'

export const Steps = (StepContent) => {
    return (
        <>
            <Segment>
                <Container textAlign={'center'}>
                    <Header as='h3'> GREENSTEP </Header>
                    <p> Let us give you the exact Route for your GREENSTEP</p>
                </Container>
            </Segment>
            {/*<Step.Group fluid>*/}
            {/*    {renderSteps(StepContent)}*/}
            {/*</Step.Group>*/}
        </>
    )
};

export const StepsLoader = (StepContent) => {
    return (
        <Fragment>
            <div>
                <Segment attached>
                    <Loader active/>
                    <Image src='https://react.semantic-ui.com/images/wireframe/paragraph.png'/>
                </Segment>
            </div>
        </Fragment>
    )
};

export const renderSteps = (StepContent) => {
    Object.keys(StepContent).map((key, value) => {
        return (
            <Step key={key}>
                <Icon name={StepContent.Icons[value]}/>
                <Step.Content>
                    <Step.Title>{StepContent.Header[value]}</Step.Title>
                    <Step.Description>{StepContent.Description[value]}</Step.Description>
                </Step.Content>
            </Step>
        )
    });
};

